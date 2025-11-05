from celery import shared_task
from .utils import fetch_sap_attendance, fetch_jira_tickets, fetch_gitlab_commits, calculate_kpis

@shared_task
def sync_data_and_calculate_kpis():
    fetch_sap_attendance()
    fetch_jira_tickets()
    fetch_gitlab_commits()
    calculate_kpis()  # Calculate and store KPIs after syncing