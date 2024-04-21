# urls.py

from django.urls import path
from books.views import add_book

urlpatterns = [
    path('add-book/', add_book, name='add_book'),
    # Other URL patterns for your project
]
