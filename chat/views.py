from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.







def signUp(request):
    return render(request, "login/signup.html")

def login(request):
    return render(request, "login/login.html")

def home(request):
    return render(request, "home.html")