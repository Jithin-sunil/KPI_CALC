from django.db import models

# Create your models here.

class tbl_employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_email = models.EmailField()
    employee_phone = models.CharField(max_length=15)
    employee_designation = models.CharField(max_length=150)
    employee_department = models.CharField(max_length=150)
    employee_join_date = models.DateField()
    employee_password=models.CharField(max_length=50,null=True)

