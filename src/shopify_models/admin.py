import sys
from django.contrib import admin, messages
import requests
import traceback
import json
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register your models here.
from .models import Product, Page, Template
from skripte.models import Skripta, Section
from problems.models import Problem
from mature.models import Matura
from api.serializers import ShopifyPageSkriptaListSerializer, ShopifyPageProblemSerializer, ShopifyPageSkriptaSerializer, ShopifyProductMaturaSerializer

from django.conf import settings


class SkriptaInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Skripta
    extra = 0

class MaturaInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Matura
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        MaturaInline,
    ]
    actions = ['delete_pages', 'update_tabs', 'create_product']
    
    @admin.action(description='Update matura product on Shopify')
    def update_tabs(self, request, queryset):
        headers = {
            'Content-Type': 'application/json', 
            'X-Shopify-Access-Token': settings.SHOPIFY_ACCESS_TOKEN }

        for product in queryset:
            metafields_url = '/admin/api/{api_version}/products/{id}/metafields.json'.format(id=product.product_id, api_version=settings.SHOPIFY_API_VERSION)
            maturas = Matura.objects.filter(product=product).order_by('term')
            matura_tabs = []

            for matura in maturas:
                serializer = ShopifyProductMaturaSerializer(matura, many=False)
                matura_tabs.append(serializer.data)

            json_string = json.dumps(matura_tabs)

            metafield_data = {
                "metafield": {
                        "namespace": "matura",
                        "key": "tabs",
                        "type": "json",
                        "value": json_string,
                    }
                }
            url = settings.SHOPIFY_STORE_URL + metafields_url
            try:
                response = requests.post(url, headers=headers, json = metafield_data)
                print(response.json())
                messages.success(request, "Proizvod {p} uspješno ažuriran sa {n} tab-a".format(p = product, n = len(matura_tabs)))
            except:
                messages.error(request, "Nešto je krepalo. Error: {e}.".format(e=sys.exc_info()[0]))

    @admin.action(description='Create product on Shopify')
    def create_product(self, request, queryset):
        headers = {
            'Content-Type': 'application/json', 
            'X-Shopify-Access-Token': settings.SHOPIFY_ACCESS_TOKEN
        }
        products_url = '/admin/api/{api_version}/products.json'.format(api_version=settings.SHOPIFY_API_VERSION)

        for product in queryset:
            if(product.id == None):
                # seo_title = "{n} - Rješenja mature {m} | Gradivo.hr".format(n = product.title.split(' - ')[0], m = product.title.split(' - ')[1])
                # seo_description = "Preko Preko 70 videa s u potpunosti riješenim i objašnjenim svim zadatcima iz mature iz kemije {y} godine (ljetni i jesenski rok)".format( y = product.title.split(' - ')[1] )
                product_data = {
                    "product": {
                        "title": product.title,
                        "product_type": product.type if product.type != None else "",
                        "vendor": product.vendor if product.vendor != None else "",
                        "published": False,
                        "status": "draft",
                        "metafields_global_title_tag": product.seo_title if product.seo_title != None else "",
                        "metafields_global_description_tag": product.seo_description if product.seo_description != None else "",                        
                    }
                }
                url = settings.SHOPIFY_STORE_URL + products_url
                try:
                    response = requests.post(url, headers = headers, json = product_data)
                    print('response: ', response.json())
                    data = response.json()['product']
                    product.product_id = data['id']
                    product.handle = data['handle']
                    product.graphql_api_id = data['admin_graphql_api_id']
                    product.save()
                    messages.success(request, "Proizvod {prod} uspješno kreiran sa Shopify-a".format(prod=product.title))
                except:
                    messages.error(request, "Proizvod {prod} NIJE uspješno kreiran. Error: {err}".format(prod=product.title, err=sys.exc_info()[0]))
            else:
                messages.error(request, "Proizvod vec postoji na Shopify-u".format(prod=product.title))
        

class PageAdmin(admin.ModelAdmin):
    actions = ['delete_pages', 'update_page_content',]
    list_filter = ('template',)

    inlines = [
        SkriptaInline,
    ]

    @admin.action(description='Create selected pages on Shopify')
    def create_pages(self, request, queryset):
        return 1

    @admin.action(description='OPREZNO!!!! Delete selected pages from Shopify')
    def delete_pages(self, request, queryset):
        headers = { 
            'Content-Type': 'application/json', 
            'X-Shopify-Access-Token': settings.SHOPIFY_ACCESS_TOKEN
        }
        pages = queryset
        for page in pages:
            delete_url = '/admin/api/{api_version}/pages/{page_id}.json'.format(page_id=page.page_id, api_version=settings.SHOPIFY_API_VERSION)
            url = settings.SHOPIFY_STORE_URL + delete_url
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
        headers = {
            'Content-Type': 'application/json', 
            'X-Shopify-Access-Token': settings.SHOPIFY_ACCESS_TOKEN
        }

        for page in queryset:
            page_url = '/admin/api/{api_version}/pages/{id}/metafields.json'.format(id=page.page_id, api_version=settings.SHOPIFY_API_VERSION)
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
                url = settings.SHOPIFY_STORE_URL + page_url
                try:
                    response = requests.post(url, headers=headers, json = metafield_data)
                    messages.success(request, "Page {page} uspješno ažuriran sa skriptama".format(page=skripta.page.title))
                except:
                    messages.error(request, "Page {page} neuspješno ažuriran. Error: {err}".format(page=skripta.page.title, err=sys.exc_info()[0]))

            
            try:
                section = Section.objects.get(page=page)

                if(section):
                    skripta_section = Skripta.objects.filter(skriptasection__section__id = section.id)
                    problems_list = []

                    for skripta in skripta_section:
                        problems = Problem.objects.filter(section = section, skripta__id = skripta.id )
                        serilizer = ShopifyPageProblemSerializer(problems, many=True)
                        skripta_serializer = ShopifyPageSkriptaSerializer(skripta, many=False)
                        problems_list.append({
                            'skripta': skripta_serializer.data,
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
                    url = settings.SHOPIFY_STORE_URL + page_url

                    try:
                        response = requests.post(url, headers=headers, json = metafield_data)
                        messages.success(request, "Page {page} uspješno ažuriran sa zadatcima".format(page=page.title))
                    except:
                        messages.error(request, "Page {page} neuspješno ažuriran. Error: {err}".format(page=page.title, err=traceback.format_exc()))
            except:
                messages.error(request, "Page {page} nema section?. Error: {err}".format(page=page.title, err=sys.exc_info()[0]))




        
    

# class ProductAdmin(admin.ModelAdmin):



admin.site.register(Page, PageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Template)