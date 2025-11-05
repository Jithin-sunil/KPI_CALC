from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class KPI(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)  # e.g., "Ticket Completion Rate"
    value = models.FloatField()
    date_calculated = models.DateField()
    period = models.CharField(max_length=20)  # e.g., "Daily", "Weekly"

    def __str__(self):
        return f"{self.metric_name} for {self.employee.name}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.FloatField()
    leave_type = models.CharField(max_length=50, null=True)

class JiraTicket(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    ticket_id = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    story_points = models.IntegerField(null=True)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True)

class GitLabCommit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    project_id = models.CharField(max_length=50)
    commit_date = models.DateTimeField()
    lines_added = models.IntegerField()
    lines_deleted = models.IntegerField()