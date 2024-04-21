from django.shortcuts import render, redirect
from .models import Book

def add_book(request):
    if request.method == 'POST':
        author_name = request.POST['author_name']
        book_name = request.POST['book_name']
        publish_date = request.POST['publish_date']
        description = request.POST['description']
        price = request.POST['price']
        cover_photo = request.FILES['cover_photo']
        logo = request.FILES['logo']

        Book.objects.create(
            author_name=author_name,
            book_name=book_name,
            publish_date=publish_date,
            description=description,
            price=price,
            cover_photo=cover_photo,
            logo=logo
        )
        return redirect('index')  # Redirect to a success page
    return render(request, 'create_book.html')
