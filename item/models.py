from django.db import models

class item(models.Model):
    item_title = models.CharField(max_length=150)
    item_desc = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='images/')
# Create your models here.

class ItemDetails(models.Model):
    item_details_title = models.CharField(max_length=100)
    item_details_desc = models.CharField(max_length=250)
    item_details_images = models.ImageField(upload_to='images/')
    
    
class ItemDetails1(models.Model):
    item_details1_title = models.CharField(max_length=100)
    item_details1_desc = models.CharField(max_length=250)
    item_details1_images = models.ImageField(upload_to='images/')   