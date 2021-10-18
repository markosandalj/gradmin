from django.contrib import admin
from django.contrib import messages
import requests

# Register your models here.
from .models import Product, Page, Template

class PageAdmin(admin.ModelAdmin):
    actions = ['publish_pages', 'hide_pages', 'delete_pages',]

    @admin.action(description='OPREZNO!!!! Delete selected pages from Shopify')
    def delete_pages(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        pages = queryset
        for page in pages:
            delete_url = '/admin/api/2021-10/pages/{page_id}.json'.format(page_id=page.page_id)
            url = base_url + delete_url
            response = requests.delete(url, headers=headers)
            print('response: ', response.json())
            messages.success(request, "Stranica {str} uspješno obrisana sa Shopify-a".format(str=page.title))
            page.delete()

    @admin.action(description='Publish selected pages on Shopify')
    def publish_pages(self, request, queryset):
        return 1

    @admin.action(description='Hide selected pages on Shopify')
    def hide_pages(self, request, queryset):
        return 1
    

# class ProductAdmin(admin.ModelAdmin):



admin.site.register(Page, PageAdmin)
admin.site.register(Product)
admin.site.register(Template)