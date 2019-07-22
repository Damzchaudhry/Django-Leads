"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static


from user.views import *
from resume.views import *

from appli.views import *


from article import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('',views.index,name = "index"),
    path('about/',views.about,name = "about"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path('appli/',include("appli.urls")),
    path('resume/',include("resume.urls")),





]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
