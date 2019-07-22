from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('forgots/',views.forgot,name = "forgots"),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('validate_email/', views.validate_email, name='validate_email'),



]
