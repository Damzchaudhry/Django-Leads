from django import forms
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
import re

class LoginForm(forms.Form):
    username = forms.CharField(label = "Enter Username")
    password = forms.CharField(label = "Enter Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):

    username = forms.CharField(max_length = 50,label = "Enter Username")
    password = forms.CharField(min_length=8,max_length=20,label = "Enter Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm Password",widget = forms.PasswordInput)
    email =forms.EmailField(label="Enter Email")
    




    def clean(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exist")


        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exist")
 

 
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        user = authenticate(auth_user='username')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("password not match")
        
        if len("password") <=  4:
            raise forms.ValidationError("password is too short !!!")

            
        values = {
            "username" : username,
            "password" : password,
            "email"    : email
        }
        return values


