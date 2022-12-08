from django.shortcuts import render
from django.http import HttpResponse
from chat.models import userDetails


# Create your views here.

# for signup

def signUp(request):
    if request.method == "POST":
        firstName = request.POST.get("fname")
        lastName = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if userDetails.objects.filter(email=email, password=password):
                return HttpResponse("User already exists")
        else:
            userAuth = userDetails(firstName=firstName, lastName = lastName, email=email, password = password)
            userAuth.save()
            return render(request, "login/login.html")
            
    

    else:
        return render(request, "login/signup.html")


#login logic
def login(request):

    if request.method== "POST":
        return userAuth(request)

    else:
        return render(request, "login/login.html")

def home(request, user):
    contex={"user": user.firstName}
    return render(request, "home.html", contex)






# *****non page logics************
#To Check if the user is registered


    
#Authorization function
def userAuth(request):     
    email=  request.POST.get("email")
    password = request.POST.get("password")

    return userCheck(email, password, request)

def userCheck(email, password, request):
    try: 
        user =userDetails.objects.get(email=email, password=password)
    except: 
        user= False
    
    
    if user:
        
        return home(request, user)
    else:
        return HttpResponse("user not found")


       