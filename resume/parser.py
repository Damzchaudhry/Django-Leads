from io import StringIO
import io
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Resume,Upload_resume
from django.contrib import messages
import sys
import re
import os
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from django.core.files.storage import FileSystemStorage




from django.conf import settings


	
def pas(request):
	return redirect("resume:pr")




def pr(request):
	file=Upload_resume.objects.first()
	pdf_path  = os.path.join(settings.MEDIA_ROOT, str(file.resume))





	d = os.path.join(settings.STATIC_ROOT, "d.txt")
	resource_manager = PDFResourceManager()
	fake_file_handle = StringIO()
	converter = TextConverter(resource_manager, fake_file_handle)
	page_interpreter = PDFPageInterpreter(resource_manager, converter)

	with open(pdf_path, 'rb') as fh:
		for page in PDFPage.get_pages(fh, 
		                              caching=True,
		                              check_extractable=True):
		    page_interpreter.process_page(page)

		text = fake_file_handle.getvalue()

		f = open(d, "a",encoding="utf-8")
		f.truncate(0)
		f.write(text)
		f.close()

	   
	# close open handles
	converter.close()
	fake_file_handle.close()



	 
	if __name__ == '__main__':
	    print(extract_text_from_pdf(pdf_path))

	fileToWrite = os.path.join(settings.STATIC_ROOT,"pr.txt")


	fileToRead = os.path.join(settings.STATIC_ROOT, "d.txt")

	 
	delimiterInFile = [',', ';']
	 
	def validateEmail(strEmail):
	    # .* Zero or more characters of any type. 
	    if re.findall(r"[^@]+@[^@]+\.[^@]+", strEmail):
	        try:
	            return strEmail[0].split()[0].strip(';')
	        except IndexError:
	            return none
	 
	def writeFile(listData):
	    file = open(fileToWrite, 'w+',encoding="utf-8")
	    strData = ""
	    for item in listData:
	        strData = strData+item+'\n'
	    file.write(strData)
	 
	listEmail = []
	file = open(fileToRead, 'r',encoding="utf-8") 
	listLine = file.readlines()

	for itemLine in listLine:
	    item =str(itemLine)
	    for delimeter in delimiterInFile:
	        item = item.replace(str(delimeter),' ')
	     
	    wordList = item.split()
	    for word in wordList:
	        if(validateEmail(word)):
	            listEmail.append(word)
	 
	if listEmail:
	    uniqEmail = set(listEmail)
	    print(len(uniqEmail),"emails collected!")
	    writeFile(uniqEmail)
	else:
	    print("No email found.")


# ---------------------------------Phone-------------------------------------------------

	fileToWrite_phone = os.path.join(settings.STATIC_ROOT,"phone.txt")


	fileToRead = os.path.join(settings.STATIC_ROOT, "d.txt")

	 
	delimiterInFile = [',', ';']
	 
	def validate_phone(strPhone):
	    # .* Zero or more characters of any type. 
	    if re.findall(r"^(\+\d{1,3})?,?\s?\d{8,13}", strPhone):
	        try:
	            return strPhone[0].split()[0].strip(';')
	        except IndexError:
	            return none
	 
	def writeFile(listData):
	    file = open(fileToWrite_phone, 'w+',encoding="utf-8")
	    strData = ""
	    for item in listData:
	        strData = strData+item+'\n'
	    file.write(strData)
	 
	listPhone = []
	file = open(fileToRead, 'r',encoding="utf-8") 
	listLine = file.readlines()

	for itemLine in listLine:
	    item =str(itemLine)
	    for delimeter in delimiterInFile:
	        item = item.replace(str(delimeter),' ')
	     
	    wordList = item.split()
	    for word in wordList:
	        if(validate_phone(word)):
	            listPhone.append(word)
	 
	if listPhone:
	    uniqPhone = set(listPhone)
	    print(len(uniqPhone),"Phone collected!")
	    writeFile(uniqPhone)
	else:
	    print("No Phone found.")

    
	messages.success(request,"CV successfully Uploaded")
	return redirect("resume:Res")





	#--------------------------------------------------Phone


