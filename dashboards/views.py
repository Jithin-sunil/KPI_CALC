from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import KPISerializer
from integrations.models import KPI, Employee
from .models import *
from Guest.models import *
import random,json
import openpyxl
from datetime import datetime

@api_view(['GET'])
def employee_kpi_summary(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        kpis = KPI.objects.filter(employee=employee)
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

def kpi_dashboard(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        kpis = KPI.objects.filter(employee=employee)
        labels = [kpi.metric_name for kpi in kpis]
        data = [kpi.value for kpi in kpis]
        return render(request, 'dashboards/kpi_dashboard.html', {'employee': employee, 'labels': labels, 'data': data})
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)


def employee(request):
    emp=tbl_employee.objects.all()
    if request.method == 'POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        dob=request.POST.get('txt_dob')
        tbl_employee.objects.create(employee_name=name,employee_email=email,employee_dob=dob)
        return render(request, 'dashboards/employee.html',{'msg':'Employee Added Successfully'})
    else:
        return render(request, 'dashboards/employee.html',{'emp':emp})


def dashboard(request):
    # Demo data for 10 employees (September 2025, 4-week month)
    employees = [
        {"name": "Alice Smith", "ticket_completion_percent": 95, "story_points_delivered": 40, "commits_per_week": 15},
        {"name": "Bob Johnson", "ticket_completion_percent": 80, "story_points_delivered": 30, "commits_per_week": 10},
        {"name": "Carol White", "ticket_completion_percent": 90, "story_points_delivered": 36, "commits_per_week": 12},
        {"name": "David Brown", "ticket_completion_percent": 85, "story_points_delivered": 32, "commits_per_week": 8},
        {"name": "Emma Davis", "ticket_completion_percent": 100, "story_points_delivered": 44, "commits_per_week": 20},
        {"name": "Frank Wilson", "ticket_completion_percent": 75, "story_points_delivered": 24, "commits_per_week": 6},
        {"name": "Grace Lee", "ticket_completion_percent": 92, "story_points_delivered": 38, "commits_per_week": 14},
        {"name": "Henry Taylor", "ticket_completion_percent": 88, "story_points_delivered": 34, "commits_per_week": 11},
        {"name": "Isabella Moore", "ticket_completion_percent": 98, "story_points_delivered": 42, "commits_per_week": 18},
        {"name": "James Clark", "ticket_completion_percent": 70, "story_points_delivered": 20, "commits_per_week": 5}
    ]
    
    # Prepare data for Chart.js
    chart_data = {
        'labels': [employee['name'] for employee in employees],
        'datasets': [
            {
                'label': 'Ticket Completion Rate (%)',
                'data': [employee['ticket_completion_percent'] for employee in employees],
                'backgroundColor': 'rgba(54, 162, 235, 0.6)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Monthly Story Points Delivered',
                'data': [employee['story_points_delivered'] for employee in employees],
                'backgroundColor': 'rgba(255, 99, 132, 0.6)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Commits per Week',
                'data': [employee['commits_per_week'] for employee in employees],
                'backgroundColor': 'rgba(75, 192, 192, 0.6)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }
        ]
    }
    
    
    context = {
        'chart_data': chart_data,
        'month': 'September 2025'
    }
    return render(request, 'dashboards/kpi_dashboard.html', context)

    




def dashboard(request):
    employees = ["Alice", "Bob", "Charlie", "David", "Evelyn", 
                 "Frank", "Grace", "Hannah", "Ivy", "Jack"]

    # Existing 5
    attendance = [250, 240, 230, 220, 255, 245, 235, 250, 225, 260]
    tickets = [120, 110, 95, 105, 130, 100, 90, 115, 85, 140]
    commits = [780, 650, 540, 500, 810, 600, 450, 700, 400, 900]
    leaves = [10, 15, 20, 18, 8, 12, 14, 10, 22, 5]
    bugs = [40, 35, 28, 30, 45, 32, 25, 38, 20, 50]

    # Extra 10
    overtime = [120, 80, 150, 100, 90, 110, 95, 130, 70, 140]
    effective_days = [240, 225, 210, 202, 247, 233, 221, 240, 203, 255]
    attendance_rate = [96, 92, 88, 85, 98, 94, 90, 95, 87, 99]
    story_points = [300, 280, 260, 270, 350, 290, 240, 310, 200, 370]
    close_time = [2.5, 3.2, 4.0, 3.5, 2.0, 3.8, 4.5, 2.8, 5.0, 1.9]
    reopened = [5, 7, 10, 12, 4, 8, 9, 6, 13, 3]
    merge_requests = [50, 45, 30, 28, 55, 40, 25, 48, 20, 60]
    reviews = [15, 20, 10, 12, 25, 18, 9, 22, 8, 30]
    deployments = [12, 10, 8, 6, 14, 9, 7, 11, 5, 15]
    build_fail = [3, 5, 7, 6, 2, 4, 8, 5, 9, 1]

    context = {
        "employees": json.dumps(employees),
        "attendance": json.dumps(attendance),
        "tickets": json.dumps(tickets),
        "commits": json.dumps(commits),
        "leaves": json.dumps(leaves),
        "bugs": json.dumps(bugs),
        "overtime": json.dumps(overtime),
        "effective_days": json.dumps(effective_days),
        "attendance_rate": json.dumps(attendance_rate),
        "story_points": json.dumps(story_points),
        "close_time": json.dumps(close_time),
        "reopened": json.dumps(reopened),
        "merge_requests": json.dumps(merge_requests),
        "reviews": json.dumps(reviews),
        "deployments": json.dumps(deployments),
        "build_fail": json.dumps(build_fail),
    }
    return render(request, "dashboards/kpi_dashboard.html", context)

def adminregister(request):
    if request.method == 'POST':
        admin_name = request.POST.get('admin_name')
        admin_email = request.POST.get('admin_email')
        admin_password = request.POST.get('admin_password')
        tbl_admin.objects.create(
            admin_name=admin_name,
            admin_email=admin_email,
            admin_password=admin_password
        )
        return redirect('dashboards:adminregister')
    else:
        return render(request, 'dashboards/adminregister.html')
    


def employee_register(request):

    if request.method == "POST":
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            name, email, phone, designation, department, join_date = row

            if isinstance(join_date, datetime):
                join_date = join_date.date()

            emp = tbl_employee.objects.filter(
                employee_name=name,
                employee_email=email
            ).first()

            if emp:
                emp.employee_phone = phone
                emp.employee_designation = designation
                emp.employee_department = department
                emp.employee_join_date = join_date
                emp.save()

            else:
                part1 = (name[:3] if name else "emp").lower()
                part2 = (designation[:3] if designation else "des").lower()
                part3 = (department[:3] if department else "dep").lower()

                import random
                pwd = part1 + part2 + part3 + str(random.randint(100, 999))

                tbl_employee.objects.create(
                    employee_name=name,
                    employee_email=email,
                    employee_phone=str(phone),
                    employee_designation=designation,
                    employee_department=department,
                    employee_join_date=join_date,
                    employee_password=pwd
                )

        return render(request, "dashboards/employee_register.html", {
            "success": "Employee data uploaded and updated successfully!"
        })

    return render(request, "dashboards/employee_register.html")

    
def employee_list(request):
    employees = tbl_employee.objects.all()

    return render(request, "dashboards/employee_list.html", {
        "employees": employees
    })