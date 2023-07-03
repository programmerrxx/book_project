from django.urls import path
from .views import AllNewsView, DetailsNewsView, CreateNewsView, UpdateNewsView, DeleteNewsView
from .views import AllAuthorView, DetailsAuthorView, CreateAuthorView, UpdateAuthorView, DeleteAuthorView

urlpatterns = [
    path('', AllNewsView.as_view()),
    path('news/', AllNewsView.as_view()),
    path('news/<int:news_id>', DetailsNewsView.as_view()),
    path('news/create/', CreateNewsView.as_view()),
    path('news/update/<int:news_id>/', UpdateNewsView.as_view()),
    path('news/delete/<int:news_id>/', DeleteNewsView.as_view()),

    path('author/', AllAuthorView.as_view()),
    path('author/<int:author_id>', DetailsAuthorView.as_view()),
    path('author/create/', CreateAuthorView.as_view()),
    path('author/update/<int:author_id>/', UpdateAuthorView.as_view()),
    path('author/delete/<int:author_id>/', DeleteAuthorView.as_view()),
]