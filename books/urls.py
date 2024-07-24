# urls.py

from django.urls import path
from books.views import add_book,delete_book

urlpatterns = [
    path('add-book/', add_book, name='add_book'),
    path('delete_book/<int:pk>', delete_book, name='delete_book')
    # Other URL patterns for your project
]
