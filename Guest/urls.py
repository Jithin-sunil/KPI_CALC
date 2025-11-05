from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('contact/',views.contact,name="contact"),
    # path('login/',views.login,name="login"),


]