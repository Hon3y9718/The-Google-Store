from django.contrib import admin
from django.urls import include, path
from adminApp import views

urlpatterns = [
    path('adminApp/sudo/login', views.adminLogin, name='Admin Home')
]