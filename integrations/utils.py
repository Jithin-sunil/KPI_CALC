import requests
from jira import JIRA
import gitlab
from datetime import datetime
from .models import Attendance, JiraTicket, GitLabCommit, KPI, Employee

# Replace with actual API details
SAP_URL = "https://sap-api.example.com/attendance"
SAP_AUTH = ("user", "pass")
JIRA_SERVER = "https://jira.example.com"
JIRA_AUTH = ("user", "pass")
GITLAB_URL = "https://gitlab.example.com"
GITLAB_TOKEN = "your_token"
GITLAB_PROJECT_ID = "project_id"

def fetch_sap_attendance():
    response = requests.get(SAP_URL, auth=SAP_AUTH)
    if response.status_code == 200:
        data = response.json().get('results', [])
        for record in data:
            employee, _ = Employee.objects.get_or_create(employee_id=record['employee_id'], defaults={'name': 'Unknown', 'role': 'Developer'})
            Attendance.objects.update_or_create(
                employee=employee,
                date=record['date'],
                defaults={'hours_worked': record['hours'], 'leave_type': record.get('leave_type')}
            )

def fetch_jira_tickets():
    jira = JIRA(server=JIRA_SERVER, basic_auth=JIRA_AUTH)
    issues = jira.search_issues("project=PROJ")
    for issue in issues:
        # Assume assignee is employee; map accordingly
        employee_id = issue.fields.assignee.accountId if issue.fields.assignee else None
        if employee_id:
            employee, _ = Employee.objects.get_or_create(employee_id=employee_id, defaults={'name': issue.fields.assignee.displayName, 'role': 'Developer'})
            JiraTicket.objects.update_or_create(
                ticket_id=issue.key,
                defaults={
                    'employee': employee,
                    'status': issue.fields.status.name,
                    'story_points': issue.fields.customfield_10010,  # Adjust field ID
                    'created_at': issue.fields.created,
                    'closed_at': issue.fields.resolutiondate
                }
            )

def fetch_gitlab_commits():
    gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)
    project = gl.projects.get(GITLAB_PROJECT_ID)
    commits = project.commits.list()
    for commit in commits:
        stats = commit.stats
        # Map author_email to employee_id
        employee_id = commit.author_email
        employee, _ = Employee.objects.get_or_create(employee_id=employee_id, defaults={'name': commit.author_name, 'role': 'Developer'})
        GitLabCommit.objects.update_or_create(
            commit_date=commit.created_at,
            defaults={
                'employee': employee,
                'project_id': project.id,
                'lines_added': stats['additions'],
                'lines_deleted': stats['deletions']
            }
        )

def ticket_completion_rate(employee_id, start_date, end_date):
    tickets = JiraTicket.objects.filter(
        employee__employee_id=employee_id,
        created_at__range=[start_date, end_date]
    )
    total = tickets.count()
    closed = tickets.filter(status="Closed").count()
    return (closed / total * 100) if total else 0

def commits_per_day(employee_id, target_date):
    return GitLabCommit.objects.filter(
        employee__employee_id=employee_id,
        commit_date__date=target_date
    ).count()

def burnout_indicator(employee_id, start_date, end_date):
    overtime = Attendance.objects.filter(
        employee__employee_id=employee_id,
        date__range=[start_date, end_date],
        hours_worked__gt=8
    ).aggregate(total_overtime=models.Sum('hours_worked'))['total_overtime'] or 0
    return overtime > 20  # Threshold example

def calculate_kpis(period='Weekly'):
    # Example: Calculate for all employees
    today = datetime.now().date()
    start_date = today - datetime.timedelta(days=7) if period == 'Weekly' else today
    for employee in Employee.objects.all():
        # Ticket Completion Rate
        tcr = ticket_completion_rate(employee.employee_id, start_date, today)
        KPI.objects.create(employee=employee, metric_name="Ticket Completion Rate", value=tcr, date_calculated=today, period=period)
        
        # Commits per Day (average for period)
        commits = sum(commits_per_day(employee.employee_id, start_date + datetime.timedelta(days=i)) for i in range((today - start_date).days + 1))
        avg_commits = commits / ((today - start_date).days + 1) if (today - start_date).days else 0
        KPI.objects.create(employee=employee, metric_name="Commits per Day", value=avg_commits, date_calculated=today, period=period)
        
        # Burnout Indicator
        burnout = 1 if burnout_indicator(employee.employee_id, start_date, today) else 0
        KPI.objects.create(employee=employee, metric_name="Burnout Indicator", value=burnout, date_calculated=today, period=period)
        
        # Add more KPIs similarly...