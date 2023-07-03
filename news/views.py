from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import NewsModel, AuthorModel
from rest_framework.response import Response
from .serializers import NewsSerializer, AuthorSerializer
from rest_framework import status

# --------Author View---------

class AllAuthorView(APIView):
    def get(self,request,*args,**kwargs):
        all_author = AuthorModel.objects.all()
        serializer = AuthorSerializer(all_author,many=True)
        return Response(serializer.data)
    
class DetailsAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        news = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        serializer = AuthorSerializer(news)
        return Response(serializer.data)

class CreateAuthorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateAuthorView(APIView):
    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(AuthorModel,pk=kwargs['author_id'])
        serializer = AuthorSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)   
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class DeleteAuthorView(APIView):
    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        instance.delete()
        return Response({'message':'successfuly deleted'}, status=status.HTTP_204_NO_CONTENT)
    
# --------News View---------

class AllNewsView(APIView):
    def get(self,request,*args,**kwargs):
        all_news = NewsModel.objects.all()
        serializer = NewsSerializer(all_news,many=True)
        return Response(serializer.data)
    
class DetailsNewsView(APIView):
    def get(self, request, *args, **kwargs):
        news = get_object_or_404(NewsModel,pk=kwargs['news_id'])
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    
class CreateNewsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class UpdateNewsView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(NewsModel,pk=kwargs['news_id'])
        serializer = NewsSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)   
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class DeleteNewsView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(NewsModel, pk=kwargs['news_id'])
        instance.delete()
        return Response({'message':'successfuly deleted'}, status=status.HTTP_204_NO_CONTENT)

