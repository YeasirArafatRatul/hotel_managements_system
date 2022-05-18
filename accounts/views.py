from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.messages import success, error
from . forms import CustomUserCreationForm


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def registration(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST) 
        print("I am here")
        if form.is_valid():  
            form.save()
            success(request, 'Account created successfully')  
    else:  
        form = CustomUserCreationForm()
    context = {  
        'form':form  
    }   
    return render(request, 'registration/registration.html',context)