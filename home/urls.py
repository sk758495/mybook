# home/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_inquiry, name='saveinquiry'),

]
