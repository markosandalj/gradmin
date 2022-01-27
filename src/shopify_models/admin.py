from django.contrib import admin
from django.contrib import messages
import requests
import json

# Register your models here.
from .models import Product, Page, Template
from skripte.models import Skripta
from api.serializers import ShopifyPageSkriptaListSerializer

class PageAdmin(admin.ModelAdmin):
    actions = ['publish_pages', 'hide_pages', 'delete_pages', 'update_page_content']
    list_filter = ('template',)

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

    @admin.action(description='Update selected pages content on Shopify')
    def update_page_content(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }

        for page in queryset:
            page_url = '/admin/api/2021-10/pages/{id}/metafields.json'.format(id=page.page_id)
            skriptas = Skripta.objects.filter(page=page)
            skriptas_list = []
            
            for skripta in skriptas:
                serilizer = ShopifyPageSkriptaListSerializer(skripta)
                skriptas_list.append(serilizer.data)

            json_string = json.dumps(skriptas_list)
            metafield_data = {
                "metafield": {
                    "namespace": "section",
                    "key": "lists",
                    "type": "json",
                    "value": json_string
                }
            }
            url = base_url + page_url
            try:
                response = requests.post(url, headers=headers, json = metafield_data)
                print(response.json())
                messages.success(request, "Page {page} uspješno ažuriran".format(page=skripta.page.title))
            except:
                messages.error(request, "Page {page} neuspješno ažuriran".format(page=skripta.page.title))
    

# class ProductAdmin(admin.ModelAdmin):



admin.site.register(Page, PageAdmin)
admin.site.register(Product)
admin.site.register(Template)