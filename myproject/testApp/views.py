from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from  django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        if User.objects.filter(username = username).exists():
            messages.error(request,message="username already exists")
            return redirect("log")
        else:
            user = User.objects.create_user(username = username,password = password,email = email)
            user.save()
            messages.success(request,message="Account successfully created")
            return  redirect("log account")

    return render(request,"testApp/signIn.html")

def login(request):
    return render(request, "testApp/login.html")
