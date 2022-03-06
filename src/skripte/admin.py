from django.contrib import admin, messages
from django.db.models.fields import IntegerField
from django import forms
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
import requests
import json
from api.serializers import CategorySerialzier, ShopifyPageProblemSerializer, ShopifyPageRelatedSectionSerializer, ShopifyPageSectionSecondaryListSerializer, ShopifyPageSkriptaListSerializer
from django.db.models.functions.comparison import Cast

from shopify_models.models import Template

# Register your models here.
from .models import Category, ProblemEquation, Razred, SectionSection, SkriptaSection, Subject, Section, Equation, Skripta
from problems.models import Problem
from django.contrib.admin.helpers import ActionForm

class PickSkriptaForm(ActionForm):
    skriptas = Skripta.objects.all()
    skripta = forms.ModelChoiceField(queryset=skriptas, required=False)
    
class UpdateShopifyPageForm(ActionForm):
    templates = Template.objects.all()
    template_choices = ((x, x) for x in templates)
    template = forms.ChoiceField(choices=template_choices)

class SectionProblemInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Problem
    extra = 0
    autocomplete_fields = ('section', 'skripta', 'question',)
    exclude = ('skripta', 'subject', 'shop_availability','approval','matura', 'number')

class SectionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Section.skripta.through
    readonly_fields = ("exclude_section",)
    extra = 0

    def exclude_section(self, instance):
        return instance.section.exclude

class SectionSectionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SectionSection
    fk_name = "main_section"
    extra = 0

class ProblemEquationInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProblemEquation
    autocomplete_fields = ('equation',)
    extra=0

class SectionEquationInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Equation.section.through
    extra = 0

class SkriptaAdmin(admin.ModelAdmin):
    model = Skripta
    list_filter = ('subject',)
    list_display = ('name','id', )
    search_fields = ('name',)
    actions = ('update_shopify_page',)

    inlines = [
        SectionInline,
    ]

    @admin.action(description='Update page (online skipta - popis) on Shopify')
    def update_shopify_page(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }

        for skripta in queryset:
            page_url = '/admin/api/2021-10/pages/{id}/metafields.json'.format(id=skripta.page.page_id)
            serilizer = ShopifyPageSkriptaListSerializer(skripta)
            json_string = json.dumps(serilizer.data)
            metafield_data = {
                "metafield": {
                    "namespace": "section",
                    "key": "list",
                    "type": "json",
                    "value": json_string
                }
            }
            url = base_url + page_url
            response = requests.post(url, headers=headers, json = metafield_data)
            print(response.json())
            messages.success(request, "Page {page} uspješno ažuriran".format(page=skripta.page.title))

    
    
class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = ('name', 'icon')
    list_filter = ('subject',)
    readonly_fields = ('created_at', 'updated_at',)
    actions = ['create_shopify_page','update_problems_metafield', 'update_navigation_metafield', 'update_secondary_problems_metafield',]
    search_fields = ('name',)
    list_editable = ('icon',)
    inlines = [
        SectionProblemInline, SectionSectionInline 
    ]
    action_form = PickSkriptaForm

    @admin.action(description='Create page on Shopify')
    def create_shopify_page(self, request, queryset):
        action_form = UpdateShopifyPageForm
        base_url = 'https://msandalj23.myshopify.com'
        headers = { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        pages_url = '/admin/api/2021-10/pages.json'
        for section in queryset:
            if( not section.page.page_id ):
                template = str(request.POST['template'])
                page_data = {
                    'page': {
                        'title' : section.name,
                        'published': False,
                        'template_suffix' : template
                    }
                }
                url = base_url + pages_url
                response = requests.post(url, headers=headers, json = page_data)
                print(response.json()['page']['id'])
                section.page.page_id=response.json()['page']['id']
                section.save()
                messages.success(request, "Page for {s} created".format(s=section.name))
            else:
                messages.error(request, "Page with that id already exists")

    @admin.action(description='Update pages metafield with problems on Shopify')
    def update_problems_metafield(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        skripta_id = str(request.POST['skripta'])
        for section in queryset:
            problems = Problem.objects.annotate(number_field=Cast('number', IntegerField())).filter(section=section, approval='approved', skripta__id = skripta_id ).exclude(video_solution=None, shop_availability = 'hidden',).order_by('number_field', 'name')
            if(len(problems) > 0 ):
                serilizer = ShopifyPageProblemSerializer(problems, many=True)
                json_string = json.dumps(serilizer.data)
                metafield_data = {
                    "metafield": {
                        "namespace": "section",
                        "key": "problems",
                        "type": "json",
                        "value": json_string
                    }
                }
                page_url = '/admin/api/2021-10/pages/{id}/metafields.json'.format(id=section.page.page_id)
                url = base_url + page_url
                response = requests.post(url, headers=headers, json = metafield_data)
                print(response.json())
                messages.success(request, "Page {page} uspješno ažuriran".format(page=section.page.title))
            else:
                messages.error(request, "U gradivu {section} nema niti jedan zadatak koji zadovoljava sve uvjete.".format(section=section.name))

    @admin.action(description='Update pages metafield with secondary problems on Shopify')
    def update_secondary_problems_metafield(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        skripta_id = str(request.POST['skripta'])
        for section in queryset:
            problems = Problem.objects.annotate(number_field=Cast('number', IntegerField())).filter(section=section, approval='approved', skripta__id = skripta_id ).exclude(shop_availability='hidden', video_solution=None).order_by('number_field', 'name')
            if(len(problems) > 0 ):
                serilizer = ShopifyPageProblemSerializer(problems, many=True)
                json_string = json.dumps(serilizer.data)
                metafield_data = {
                    "metafield": {
                        "namespace": "section",
                        "key": "secondary_problems",
                        "type": "json",
                        "value": json_string
                    }
                }
                page_url = '/admin/api/2021-10/pages/{id}/metafields.json'.format(id=section.page.page_id)
                url = base_url + page_url
                response = requests.post(url, headers=headers, json = metafield_data)
                print(response.json())
                messages.success(request, "Page {page} uspješno ažuriran".format(page=section.page.title))
            else:
                messages.error(request, "U gradivu {section} nema niti jedan zadatak koji zadovoljava sve uvjete.".format(section=section.name))


    @admin.action(description='Update pages metafield with navigation on Shopify')
    def update_navigation_metafield(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        skripta_id = str(request.POST['skripta'])
        for section in queryset:
            skripta = Skripta.objects.get(id=int(skripta_id))
            try:
                skripta_section = SkriptaSection.objects.get(section=section, skripta=skripta)
                skripta_sections = SkriptaSection.objects.filter(section=section)
                skripta_tags = [ section.skripta.name for section in skripta_sections ]
                prev_section = SkriptaSection.objects.filter(skripta=skripta, section_order__lt=skripta_section.section_order).order_by('-section_order').first()
                next_section = SkriptaSection.objects.filter(skripta=skripta, section_order__gt=skripta_section.section_order).order_by('section_order').first()
                prev_section_handle = prev_section.section.page.handle if prev_section else None
                next_section_handle = next_section.section.page.handle if next_section else None
                serilizer = ShopifyPageRelatedSectionSerializer(section.related_sections.all(), many=True)
                related_sections = serilizer.data
                json_string = {
                    'prev_section' : prev_section_handle,
                    'next_section' : next_section_handle,
                    'skripta_handle' : skripta.page.handle,
                    'related_sections' : related_sections,
                    'category': CategorySerialzier(section.category).data,
                    'tags': skripta_tags
                }
                metafield_data = {
                    "metafield": {
                        "namespace": "section",
                        "key": "navigation",
                        "type": "json",
                        "value": json.dumps(json_string)
                    }
                }
                page_url = '/admin/api/2021-10/pages/{id}/metafields.json'.format(id=section.page.page_id)
                url = base_url + page_url
                response = requests.post(url, headers=headers, json = metafield_data)
                print(response.json())
                messages.success(request, "Page {page} uspješno ažuriran".format(page=section.page.title))
            except:
                messages.error(request, 'Gradivo {section} ne postoji u skripti {skripta}'.format(section=section, skripta=skripta.name))



class EquationAdmin(admin.ModelAdmin):
    model = Equation
    list_display = ('name','equation', )
    search_fields = ('name', 'equation')


admin.site.register(Equation, EquationAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Category)
admin.site.register(Razred)
admin.site.register(Subject)
admin.site.register(Skripta, SkriptaAdmin)