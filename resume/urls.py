from django.contrib import admin
from django.urls import path,include
from .import views
from .import parser
from  resume.parser import pr
from .views import Res,cv_list,Upload_cv

app_name = "resume"

urlpatterns = [
     path('Res/',views.Res,name = "Res"),
     path('pr/',parser.pr,name = "pr"),
     path('pas/',parser.pas,name = "pas"),



     path('cv_list/',views.cv_list,name = "cv_list"),
     path('resume/<int:id>',views.detail,name = "detail"),
     path('search/', views.search, name='search'),
     path('validate_email/', views.validate_email, name='validate_email'),


     path('validate_phone/',views.validate_phone,name = "validate_phone"),
     path('upload/',views.Upload_cv,name='upload'),
    # path('/',views.addArticle,name = ""),
]
