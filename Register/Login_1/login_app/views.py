from django.shortcuts import render,redirect

from .models import *

def login_name(request):
    if request.method=="POST":
        username1=request.POST['username']
        password1=request.POST['password']
        user_valid=Register_Model.objects.get(username=username1,password=password1)

        if user_valid :
            return redirect('home')
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')

def register_view(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']

        data=Register_Model(
            username=username,
            email=email,
            contact=contact,
            password=password
        )
        data.save()
        return redirect('login')

    return render(request,'loginpage.html')
