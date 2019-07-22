from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField,SerializerMethodField
from .models import Article
import django_filters

class BlogSerializer(serializers.ModelSerializer):
    author = SerializerMethodField()
    article_image = SerializerMethodField()


    url = HyperlinkedIdentityField(
        
        view_name='article:Up',
        lookup_field = 'id'
        )
    

    delete_url = HyperlinkedIdentityField(
        view_name='article:Del',
        lookup_field = 'id'
        )


    Update_url = HyperlinkedIdentityField(
        view_name='article:Up',
        lookup_field = 'id'
        )


    class Meta:
        model = Article
        fields = [
        'url','title','created_date','content','article_image','author','id','delete_url','Update_url',
        ]


    def get_author(self,obj):
        return str(obj.author.username)


   
    def get_article_image(self,obj):
        try:
            article_image=obj.article_image.path
        except:
            article_image=None

        return article_image


  


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [

            'article_image',
            'title',
            'created_date',
            'content',
            'author',
            ]
          
      


          
class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Article
        fields =[
        'id',
        'title',
        'created_date',
        'content',
        'author',
        'article_image',
        ]

        def get_id(self, obj):
            return obj.id()
            
        


