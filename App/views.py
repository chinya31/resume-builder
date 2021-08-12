from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User,auth
from .models import Resume
import pytz

import hashlib
import datetime





# Create your views here.
username1 = str()

def index(request):
   
    return render(request,"index.html")


def login(request):
   
    if request.method == "POST":
        global username1
        username1 = request.POST["username"]
        password = request.POST["password"]
        
        

        user = auth.authenticate(username=username1,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"index.html")
        else:
            print("Invalid")
            return redirect("/")

    else :
        
        return render(request,"login.html")
      


def register(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            print("username taken")
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            print("email taken")
            return redirect('/')
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            print("User created")
            return redirect('/')
    else:
        return render(request,"register.html")

def create_resume(request):
    
    if request.method=="POST":
        
        full_name=request.POST["name"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        about_you=request.POST["about"]
        education=request.POST["education"]
        career=request.POST["career"]
        skills=request.POST["skills"]
  
        try:
            
            resume = Resume.objects.get(username=username1)
            

            if resume is not None:
                resume.delete() 
        except:
            pass

        
        resume = Resume(username=username1,full_name=full_name,address=address,phone=phone,email=email,
                                about_you=about_you,education=education,career=career,skills=skills)

        
        resume.save()
        #print("done")
        
        return redirect("App:resume")
    else:
        
        return render(request,"create-resume.html")

def resume(request):

    
    try:
        resume_info = Resume.objects.get(username=username1)
        
        if resume_info==None:
            
            return render(request,"create-resume.html")
        else:
            
            context={"resume_info":resume_info}
            return render(request,"resume.html",context)
    except:
        
        return render(request,"create-resume.html")
   