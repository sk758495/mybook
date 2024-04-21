from django.contrib import admin
from item.models import item, ItemDetails, ItemDetails1

class itemAdmin(admin.ModelAdmin):
    list_display =('item_title','item_desc','item_image')
admin.site.register(item,itemAdmin) 

class item_detailsAdmin(admin.ModelAdmin):
    list_display = ('item_details_title','item_details_desc','item_details_images')
admin.site.register(ItemDetails, item_detailsAdmin)  

class item_details1Admin(admin.ModelAdmin):
    list_display = ('item_details1_title','item_details1_desc','item_details1_images')
admin.site.register(ItemDetails1, item_details1Admin)           

# Register your models here.
