from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login 
from item.models import item,ItemDetails,ItemDetails1
from books.models import Book

def index(request):        
    item_data = item.objects.all()
    item_details_data = ItemDetails.objects.all()
    item_details1_data = ItemDetails1.objects.all()
    data = {
        'item_data': item_data,
        'item_details_data': item_details_data,
        'item_details1_data': item_details1_data
    }
    return render(request, "index.html", data)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Redirect to the index page after successful login
        else:
            # Authentication failed, display an error message or handle it as needed
            error_message = "Invalid username or password. Please try again."
            return render(request, "login.html", {'error_message': error_message})
    
    return render(request, "login.html")

def submit(request):          
    return render(request,"submit.html")

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']  
        
        data = User.objects.create_user(email=email,username=username,password=password1)
        data.save()  
        return redirect('login')
        admin.site.register(User)
    return render(request,"register.html")

def forget(request):
    return render(request,"forget.html")

def contact(request):
    return render(request, 'contact.html')

def saveinquiry(request):
      return render(request, 'contact.html')


def vadodara(request):
    return render(request,"vadodara.html")
 
def photox(request):
     return render(request,"photox.html")
 
def about(request):
     return render(request,"about.html")
 
def create_book(request):
    return render(request, "create_book.html")

def book_demo(request):
    books = Book.objects.all()
    
    return render(request, "book_demo.html", {'books': books})

def dark(request):
    return render(request, "darkmode.html")
 
 