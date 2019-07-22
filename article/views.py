from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.core.paginator import Paginator
from django.shortcuts import render
from .paginator import ArticleApiPagination
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import BlogSerializer,PostCreateUpdateSerializer,BlogDetailSerializer

from django.contrib.auth.models import User

# --------------------------------------- API -------------------------------------------------




class ListBlogView(generics.ListCreateAPIView):
 
    queryset = Article.objects.all()
    serializer_class = BlogSerializer
    pagination_class = ArticleApiPagination




class PostCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=BlogDetailSerializer
    lookup_field = 'id'

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Article.objects.all()
    serializer_class=BlogDetailSerializer
    lookup_field = 'id'






# ----------------------------------  articles function -----------------------------
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        article = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"article":article})
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    article = paginator.get_page(page)

    artic=User.objects.all()

    return render(request,"articles.html",{"article":article,"artic":artic}) 

    # -----------------------------Index function-----------------------------
def index(request):
    return render(request,"index.html")



   
   #------------------------------about fun--------------------------------- 
def about(request):
    return render(request,"about.html")


    #-------------------------------Dashboard------------------------------------

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)




    #------------------------------add article--------------------------------------

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
   
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"successfully posted")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})




    #--------------------------------------Article detail--------------------------------

def detail(request,id):
    articss=User.objects.all()

    artics=Article.objects.all()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    paginator = Paginator(artics, 7) # Show 25 contacts per page
    page = request.GET.get('page')
    artic = paginator.get_page(page)

    return render(request,"detail.html",{"article":article,"comments":comments,"artic":artic,"articss":articss})

    keyword = request.GET.get("keyword")

    if keyword:
        artic = Article.objects.filter(title__contains = keyword)
        return render(request,"detail.html",{"artic":artic})

 


   



    #-------------------------------------update Article-----------------------

@login_required(login_url = "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"successfully updated")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")




 #-------------------------------delete article------------------------------
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"blog deleted")

    return redirect("article:dashboard")





    #------------------------------Addcomment-------------------------
def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
    


def galary(request):
    article=Article.objects.all()
    context={"article":article}
    return render(request,"gal.html",context)




def preview(request):
    article=Article.objects.all()
    context={"article":article}
    return render(request,"preview.html",context)
