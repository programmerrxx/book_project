from django.db import models
from datetime import datetime

class AuthorModel(models.Model):
    name = models.CharField(max_length=60, default='')
    lname = models.CharField(max_length=60, default='')
    date_of_birth = models.DateField(default=datetime.now)
    position = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'author'


class NewsModel(models.Model):
    name = models.CharField(max_length=150, default='')
    newsdata = models.CharField(max_length=900, default='')
    date_of_news = models.DateField(default=datetime.now)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'news'


