from django.contrib import admin
from django.urls import path,include
from .import views

app_name = "appli"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('get_it/', views.get_it, name="get_it"),


]
