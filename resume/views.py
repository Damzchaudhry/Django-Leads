from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Resume
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q # new
from django.conf import settings
import os

from django.contrib.auth import login,authenticate,logout
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django import forms
from django.http import HttpResponse  
from .function.functions import handle_uploaded_file  

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from io import StringIO
import io
import sys
import re

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import ResumeForm,UploadForm
from .models import Resume,Upload_resume

from .filters import CvFilter
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@login_required(login_url = "user:login")
def Res(request):
	form = ResumeForm(request.POST or None,request.FILES or None)

	if request.method=='POST':
		form = ResumeForm(request.POST or None,request.FILES or None)

		if form.is_valid():

			p = form.save(commit=False)
			p.author = request.user
			p.save()

			messages.success(request,"successfully posted")
			return redirect("index")
	# -------------------------------------------Email-----------------------------
	f = open('staticfiles/pr.txt', 'r',encoding="utf8")
	file_content = f.read()
	# -------------------------------------------Phone-----------------------------
	f.close()
	c = open('staticfiles/phone.txt', 'r',encoding="utf8")
	file_content1 = c.read()
	c.close()

	 
	return render(request,"resume.html",{"file_content1":file_content1,"file_content":file_content,"form":form})


@login_required(login_url = "user:login")
def Upload_cv(request):
	
	form = UploadForm(request.POST, request.FILES)


	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)  
		if form.is_valid():

			q = form.save(commit=False)
			q.author = request.user

			q.save()
			return redirect("resume:pas")
			
		else:
			messages.success(request,"Select a valid pdf file!!")
			return render(request,"upload.html",{'form':form})  


	return render(request,"upload.html",{'form':form})  







def cv_list(request):
	keyword = request.GET.get("keyword")
	if keyword:
		resume = Resume.objects.filter(
			Q(exp__icontains= keyword) | 
			Q(ug__icontains=keyword)   |
			Q(gender__icontains=keyword)   |
			Q(add__icontains=keyword)   |
			Q(ug_coll__icontains=keyword)   |
			Q(year_ug__icontains=keyword)   |
			Q(dob__icontains=keyword)   |
			Q(area_of_skill__icontains=keyword)   |

			Q(skill__icontains=keyword) ).distinct()
		cv_filter = CvFilter(request.GET, queryset=resume)

		return render(request,"resume_list.html",{"resume":resume})
	resume=Resume.objects.all()

	return render(request,"resume_list.html",{"resume":resume})



def detail(request,id):
	resume = get_object_or_404(Resume,id = id)
	cv  = Upload_resume.objects.all()




	return render(request,"resume_detail.html",{"resume":resume,"cv":cv})


def search(request):
	cv_list = Resume.objects.all()
	cv_filter = CvFilter(request.GET, queryset=cv_list)
	return render(request, 'resume_list.html', {'filter': cv_filter})


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Resume.objects.filter(email__iexact=email).exists()
    }

    if data['is_taken']:
        data['error_message'] = 'cv with this email already exists.'
    

    return JsonResponse(data)



def validate_phone(request):
    phone = request.GET.get('phone', None)
    data = {
        'is_taken': Resume.objects.filter(phone__iexact=phone).exists()
    }
    if data['is_taken']:
        data['error_message'] = ' Number already taken.Try another'
   

    return JsonResponse(data)