"""userproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home', views.home,name='home'),
    path('menu', views.menu, name='menu'),
    path('month', views.month,name='month'),
    path('endtotle', views.endtotle,name='endtotle'),
    path('extratotle', views.extratotle,name='extratotle'),
    path('adminlogin', views.adminlogin,name='adminlogin'),
    path('adminregister', views.adminregister,name='adminregister'),
    path('admindashbord', views.admindashbord,name='admindashbord'),
    path('addextra', views.addextra,name='addextra'),

    path('Dailytotle', views.Dailytotle,name='Dailytotle'),
    path('adminnotifi', views.adminnotifi, name='adminnotifi'),

    path('astudentlist', views.astudentlist, name='adminnotifi'),

    path('studentlogin', views.studentlogin,name='studentlogin'),
    path('studentregister', views.studentregister,name='studentregister'),
    path('logout', views.logout,name='logout'),
]
