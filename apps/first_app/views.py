from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, "first_app/index.html")

def register(request):
    return redirect('/success')
    # if(len(request.POST['First_Name']) < 2):
    #     errors.append("First name must be at least 2 characters")
    # if(len(request.POST['Last_Name']) < 2):
    #     errors.append("Last name must be at least 2 characters")
    # if(len(request.POST['Email']) < 6):
    #     errors.append("Email name must be at least 6 characters")
    # if(len(request.POST['Password']) < 2):
    #     errors.append("Password name must be at least 8 characters")   
    # else:
    #     return  
    
def login(request):
    return redirect('/success')

def success(request):
    print request.POST
    return render(request, 'first_app/success.html')

def books(request):
    return render(request, 'first_app/books.html')

def logout(request):
    return redirect('/index')

def add(request):
    return render(request, 'first_app/add.html')
