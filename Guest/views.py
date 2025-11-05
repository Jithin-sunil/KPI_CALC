from django.shortcuts import render, redirect
from Guest.models import tbl_admin
from dashboards.models import *

# Create your views here.
def index(request):
    return render(request,'Guest/index.html')

def about(request):
    return render(request,'Guest/About.html')

# def signup(request):
#     return render(request,'Guest/Signup.html')

def contact(request):
    return render(request,'Guest/contact.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_password')
        admin = tbl_admin.objects.filter(admin_email=email, admin_password=password).count()
        employee = tbl_employee.objects.filter(employee_email=email, employee_password=password).count()
        if admin >0:
            admindata = tbl_admin.objects.get(admin_email=email, admin_password=password)
            request.session['admin_id'] = admindata.id
            return redirect('dashboards:dashboard')
        elif employee > 0:
            employeedata= tbl_employee.objects.get(employee_email=email, employee_password=password)
            request.session['emp_id']= employeedata.id
            return redirect('Employee:homepage')

        else:
            return render(request, 'Guest/Signup.html', {'error': 'Invalid credentials'})
    else:
        return render(request,'Guest/Signup.html')


