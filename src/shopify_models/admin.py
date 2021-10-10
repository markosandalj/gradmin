from django.contrib import admin

# Register your models here.
from .models import Product, Page


admin.site.register(Page)
admin.site.register(Product)