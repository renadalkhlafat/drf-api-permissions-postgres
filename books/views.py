from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class BooksList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BooksDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer