from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django import forms



from io import StringIO
import io
import sys
import re

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        
        password = form.cleaned_data.get("password")
        username = form.cleaned_data.get("username")
        
        newUser = User(username =username)

        newUser.set_password(password)
        newUser.email=email
        newUser.save()
        login(request,newUser, backend='django.contrib.auth.backends.ModelBackend')
        messages.info(request,"successfully sign up...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"No match Found")
            return render(request,"login.html",context)

        messages.success(request,"")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

    
def logoutUser(request):
    logout(request)
    messages.success(request,"")
    return redirect("index")

def forgot(request):
    return render(request,"forgot.html")


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    

    return JsonResponse(data)


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }

    if data['is_taken']:
        data['error_message'] = 'This Email is already registered to different account '
    return JsonResponse(data)


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    

    return JsonResponse(data)




