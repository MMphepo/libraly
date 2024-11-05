from django.urls import path
from .views import get_books, insert_book, book_detail

urlpatterns = [
    
    path('books/', get_books, name='get_books'),
    path('books/insert/', insert_book, name='insert_book'),
    
    path('books/<int:pk>' , book_detail, name='book_details'),
]