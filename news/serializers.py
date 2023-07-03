from rest_framework import serializers
from .models import AuthorModel, NewsModel
from django.shortcuts import get_object_or_404

    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('name', 'lname', 'date_of_birth', 'position', 'country')
    
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ('id', 'name', 'newsdata', 'date_of_news', 'author')