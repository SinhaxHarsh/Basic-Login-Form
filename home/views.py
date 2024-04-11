from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import random
from .models import Post
def home(request):
    return render(request,'frontpage.html')

def register(request):
    if request.method=="POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')

        user= User.objects.create_user(username,email,password)
        user.save()
        messages.success(request,'Your Account Has Been Successfully Created')
        return redirect('signin')
    return render(request,'register.html')

def signin(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            messages.error(request,'wrong credentials')
            return redirect('home')
    return render(request,'signin.html')    

def signout(request):
    logout(request)
    return redirect('home')

def index(request):
    posts= Post.objects.all()
    return render(request,'index.html',{'post':posts})