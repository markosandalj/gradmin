from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
import requests
import json

# Register your models here.
from .models import Subject, Section, Equation, Skripta
from problems.models import Problem

class SectionProblemInline(admin.StackedInline):
    model = Problem
    extra = 0
    # search_fields = ('section', 'skripta',)
    autocomplete_fields = ('section', 'skripta', 'question',)
    # readonly_fields = ('question', )

class SectionInline(admin.StackedInline):
    model = Section.skripta.through
    extra = 0

class SkriptaAdmin(admin.ModelAdmin):
    model = Skripta
    list_filter = ('subject',)
    list_display = ('name','id', )
    search_fields = ('name',)
    
    inlines = [
        SectionInline,
    ]
class SectionAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Section
    list_display = ('name','shopify_page_id', )
    list_filter = ('subject',)
    readonly_fields = ('created_at', 'updated_at',)
    actions = ['create_shopify_page',]
    search_fields = ('name',)
    inlines = [
        SectionProblemInline,
    ]

    @admin.action(description='Create page on Shopify')
    def create_shopify_page(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        pages_url = '/admin/api/2021-10/pages.json'
        for section in queryset:
            if( section.shopify_page_id == '' ):
                page_data = {
                    'page': {
                        'title' : section.name,
                        'published': False
                    }
                }
                url = base_url + pages_url
                response = requests.post(url, headers=headers, json = page_data)
                section.update(shopify_page_id=response.json().page.id)
                print(response.json())


admin.site.register(Equation)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subject)
admin.site.register(Skripta, SkriptaAdmin)