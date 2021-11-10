from django.contrib import admin
from django.urls import path, include
from userAuth import views

urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('createAccount', views.createAccount, name='createAccount'),
]
