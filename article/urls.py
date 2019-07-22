from django.contrib import admin
from django.urls import path,include
from .import views
from .views import ListBlogView,PostCreateAPIView,PostDeleteAPIView,PostUpdateAPIView

app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addArticle/',views.addArticle,name = "addArticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete<int:id>/',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('gal/',views.galary,name = "gal"),
    path('preview/',views.preview,name = "preview"),


    path('comment/<int:id>',views.addComment,name = "comment"),
    path('blog/', ListBlogView.as_view(), name="blog"),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('deletes/<id>', PostDeleteAPIView.as_view(), name='Del'),

    path('Updates/<id>', PostUpdateAPIView.as_view(), name='Up'),






    
]
