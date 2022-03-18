from pyexpat import model
import sys
from django.contrib import admin
from django.contrib import messages
import requests
import json
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register your models here.
from .models import Product, Page, Template
from skripte.models import Skripta, Section
from problems.models import Problem
from api.serializers import ShopifyPageSkriptaListSerializer, ShopifyPageProblemSerializer


class SkriptaInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Skripta
    extra = 0

class PageAdmin(admin.ModelAdmin):
    actions = ['create_pages', 'delete_pages', 'update_page_content', 'publish_pages', 'hide_pages',]
    list_filter = ('template',)

    inlines = [
        SkriptaInline,
    ]

    @admin.action(description='Create selected pages on Shopify')
    def create_pages(self, request, queryset):
        return 1

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
            skriptas = Skripta.objects.filter(page=page).order_by('order')
            skriptas_list = []
            
            if len(skriptas) > 0:
                for skripta in skriptas:
                    serilizer = ShopifyPageSkriptaListSerializer(skripta)
                    skriptas_list.append(serilizer.data)

                skriptas_json_string = json.dumps(skriptas_list)
                metafield_data = {
                    "metafield": {
                        "namespace": "section",
                        "key": "lists",
                        "type": "json",
                        "value": skriptas_json_string
                    }
                }
                url = base_url + page_url
                try:
                    response = requests.post(url, headers=headers, json = metafield_data)
                    print(response.json())
                    messages.success(request, "Page {page} uspješno ažuriran sa skriptama".format(page=skripta.page.title))
                except:
                    messages.error(request, "Page {page} neuspješno ažuriran. Error: {err}".format(page=skripta.page.title, err=sys.exc_info()[0]))

            
            section = Section.objects.get(page=page)

            if(section):
                skripta_section = Skripta.objects.filter(skriptasection__section__id = section.id)
                problems_list = []

                for skripta in skripta_section:
                    problems = Problem.objects.filter(section = section, skripta__id = skripta.id )
                    serilizer = ShopifyPageProblemSerializer(problems, many=True)
                    problems_list.append({
                        'skripta_id': skripta.id,
                        'problems': serilizer.data
                    })

                problems_json_string = json.dumps(problems_list)
                metafield_data = {
                    "metafield": {
                        "namespace": "section",
                        "key": "problem_lists",
                        "type": "json",
                        "value": problems_json_string
                    }
                }
                url = base_url + page_url

                try:
                    response = requests.post(url, headers=headers, json = metafield_data)
                    print(response.json())
                    messages.success(request, "Page {page} uspješno ažuriran sa zadatcima".format(page=page.title))
                except:
                    messages.error(request, "Page {page} neuspješno ažuriran. Error: {err}".format(page=page.title, err=sys.exc_info()[0]))




        
    

# class ProductAdmin(admin.ModelAdmin):



admin.site.register(Page, PageAdmin)
admin.site.register(Product)
admin.site.register(Template)