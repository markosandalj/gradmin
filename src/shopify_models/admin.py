from django.contrib import admin

# Register your models here.
from .models import Product, Page

class PageAdmin(admin.ModelAdmin):
    

class ProductAdmin(admin.ModelAdmin):



admin.site.register(Page)
admin.site.register(Product)