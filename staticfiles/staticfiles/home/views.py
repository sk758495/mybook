# views.py (inside your Django app, e.g., home/views.py)

from django.shortcuts import render
from .models import ContactInquiry
from django.http import HttpResponseRedirect

# home/views.py

from django.http import HttpResponse

def success_page(request):
    return render(request, 'contact.html') 

def home(request):
    return render(request,"contact.html")


def save_inquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Create a new ContactInquiry object and save it to the database
        inquiry = ContactInquiry(name=name, email=email, phone=phone, address=address, message=message)
        inquiry.save()

        # Optionally, you can redirect the user to a success page or render a success message
        return HttpResponseRedirect('/success/')  # Change '/success/' to your desired success URL

    return render(request, 'contact.html')  # Render the contact.html template if the request method is not POST
