from django.contrib import admin
from .models import AuthorModel, NewsModel

admin.site.register(AuthorModel)
admin.site.register(NewsModel)