def handle_uploaded_file(f):  
    with open('C:/Users/Manish/Desktop/django-blog-app-master/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)