from django.urls import path
from .views import *
app_name="Employee"

urlpatterns=[
       path('', homepage, name='homepage'),

]