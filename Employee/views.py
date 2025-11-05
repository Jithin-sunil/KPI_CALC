import json
from django.shortcuts import render,HttpResponse

# Create your views here.



def employee_personal_data():
    employees = [
        {
            "name": "Alice",
            "attendance": 250,
            "tickets_closed": 120,
            "commits": 780,
            "leaves": 10,
            "bugs_resolved": 40,
            "overtime_hours": 120,
            "effective_days": 240,
            "attendance_rate": 96,
            "story_points": 300,
            "avg_close_time": 2.5,
            "reopened_tickets": 5,
            "merge_requests": 50,
            "reviews_done": 15,
            "deployments": 12,
            "build_failures": 3,
        },
        {
            "name": "Bob",
            "attendance": 240,
            "tickets_closed": 110,
            "commits": 650,
            "leaves": 15,
            "bugs_resolved": 35,
            "overtime_hours": 80,
            "effective_days": 225,
            "attendance_rate": 92,
            "story_points": 280,
            "avg_close_time": 3.2,
            "reopened_tickets": 7,
            "merge_requests": 45,
            "reviews_done": 20,
            "deployments": 10,
            "build_failures": 5,
        },

        # ✅ Continue for all 10 employees...

        {
            "name": "Jack",
            "attendance": 260,
            "tickets_closed": 140,
            "commits": 900,
            "leaves": 5,
            "bugs_resolved": 50,
            "overtime_hours": 140,
            "effective_days": 255,
            "attendance_rate": 99,
            "story_points": 370,
            "avg_close_time": 1.9,
            "reopened_tickets": 3,
            "merge_requests": 60,
            "reviews_done": 30,
            "deployments": 15,
            "build_failures": 1,
        }
    ]

    return employees



def homepage(request):
    employees = employee_personal_data()

    context = {
        "employees": employees,
        "js_employees": json.dumps([e["name"] for e in employees]),
        "attendance": json.dumps([e["attendance"] for e in employees]),
        "tickets": json.dumps([e["tickets_closed"] for e in employees]),
        "commits": json.dumps([e["commits"] for e in employees]),
        "leaves": json.dumps([e["leaves"] for e in employees]),
        "bugs": json.dumps([e["bugs_resolved"] for e in employees]),
        "overtime": json.dumps([e["overtime_hours"] for e in employees]),
        "effective_days": json.dumps([e["effective_days"] for e in employees]),
        "attendance_rate": json.dumps([e["attendance_rate"] for e in employees]),
        "story_points": json.dumps([e["story_points"] for e in employees]),
        "close_time": json.dumps([e["avg_close_time"] for e in employees]),
        "reopened": json.dumps([e["reopened_tickets"] for e in employees]),
        "merge_requests": json.dumps([e["merge_requests"] for e in employees]),
        "reviews": json.dumps([e["reviews_done"] for e in employees]),
        "deployments": json.dumps([e["deployments"] for e in employees]),
        "build_fail": json.dumps([e["build_failures"] for e in employees]),
    }

    return render(request, "dashboards/kpi_dashboard.html", context)
