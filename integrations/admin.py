from django.contrib import admin
from .models import Employee, KPI, Attendance, JiraTicket, GitLabCommit

admin.site.register(Employee)
admin.site.register(KPI)
admin.site.register(Attendance)
admin.site.register(JiraTicket)
admin.site.register(GitLabCommit)