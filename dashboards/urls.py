from django.urls import path
from .views import employee_kpi_summary, kpi_dashboard,employee, dashboard, adminregister,employee_register,employee_list,upload_employee_excel
app_name = 'dashboards'

urlpatterns = [
    path('kpis/<str:employee_id>/', employee_kpi_summary, name='employee_kpi_summary'),
    path('dashboard/<str:employee_id>/', kpi_dashboard, name='kpi_dashboard'),
    path('Employee/',employee,name='employee'),
    path('', dashboard, name='dashboard'),
    path('adminregister/', adminregister, name='adminregister'),
    path('employee_register/', employee_register, name='employee_register'),
    path('employee_list/', employee_list, name='employee_list'),
    path('upload_employee_excel/', upload_employee_excel, name='upload_employee_excel'),
]