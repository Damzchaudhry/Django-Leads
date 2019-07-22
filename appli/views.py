from django.shortcuts import render
import requests
def get_it(request):
	return render(request,"apiform.html")

def home(request):
	if request.method == 'POST':
		ids = request.POST.get('id', None)
		if(ids !=None):
			response = requests.get('http://127.0.0.1:8000/articles/Updates/'+ids+'?format=json')
			geodata = response.json()
			return render(request, "extra.html", {
		    	'id': geodata['id'],
                'created_date':geodata['created_date'],
                'article_image':geodata['article_image'],
                'author':geodata['author']
                })




    