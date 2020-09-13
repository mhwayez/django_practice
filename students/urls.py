from django.contrib import admin
from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    
    path('',views.home,name = 'home'),
    path('wayez/',views.wayez_details, name='wayez_details'),
    path('template_wayez/',views.template_wayez, name = 'template'),
    path('form/',views.form,name="form"),

]
