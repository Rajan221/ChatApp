from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

# for signup

def signUp(request):
    
    return render(request, "login/signup.html")

def login(request):
    if request.method =="POST":
        return render(request, "home.html")
        
    else:
        return render(request, "login/login.html")

def home(request):
    return render(request, "home.html")