from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
# Create your views here.


def index( request ):
    # if request.method == 'POST':
        # check user has entered credential

    return render(request,'adminstudent.html')

def home( request ):
    return render(request,'base1.html')



def adminlogin( request ):
    return render(request,'adminlogin.html')

def adminregister( request ):
    return render(request, 'adminregister.html')

def admindashbord( request ):
    return render(request, 'admindashbord.html')

def addextra( request ):
    return render(request, 'addextra.html')

def adminnotifi( request ):
    return render(request, 'adminnotifi.html')

def astudentlist( request ):
    return render(request, 'astudentlist.html')



def Dailytotle( request ):
    return render(request, 'Dailytotle.html')

def studentlogin( request ):
    return render(request,'studentlogin.html')

def studentregister( request ):
    return render(request,'studentregister.html')

def logout(request):
    return  render(request,'adminstudent.html')


def menu(request):
    return  render(request,'menu.html')

def month(request):
    return  render(request,'monthlytotle.html')

def endtotle(request):
    return  render(request,'endtotle.html')

def extratotle(request):
    return  render(request,'extratotle.html')



