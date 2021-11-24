from django.urls import path
from .views import BooksList, BooksDetail

urlpatterns = [
    path('', BooksList.as_view(), name='books_list'),
    path('<int:pk>/', BooksDetail.as_view(), name='books_detail'),
    ]