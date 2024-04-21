"""
URL configuration for pract project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pract import views
from django.conf import settings
from django.conf.urls.static import static
from home.views import success_page
from django.views.generic import RedirectView
from django.conf.urls.static import static
from books.views import add_book






urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.login,name='login'),
    path('login/', views.register, name='register'),
    path('forget/', views.forget, name='forget'),
    path('submit/', views.submit, name='submit'),
    path('contact_us/',views.contact, name='contact'),
    path('saveinquiry/',views.contact, name='saveinquiry'),
    path('vadodara/',views.vadodara, name='vadodara'),
    path('photox/',views.photox, name='photox'),
    path('home/',include('home.urls'),name='home'),
    path('success/', success_page, name='success'),    
    path('success/', RedirectView.as_view(url='/contact/', permanent=False)),   
    path('about/', views.about, name='about'),
    
    path('create_book/',views.create_book, name='book'),
    path('', include('books.urls')),
    
    path('bookdemo/', views.book_demo, name='demo'),
    path('dark/', views.dark, name='dark'),
    
    


    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
