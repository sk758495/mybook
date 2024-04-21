from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from item.models import item,ItemDetails,ItemDetails1

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
        try:
            return HttpResponseRedirect('/index/')
        except:
            pass    
    return render(request,"login.html")    

def submit(request):          
    return render(request,"submit.html")

def register(request):
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
 
 