from django.contrib import admin

from mature.models import Matura, MaturaSubject, Term, Year
from problems.models import Problem, Question
from django.urls import reverse
from django.utils.safestring import mark_safe
from api.serializers import ProblemSerializer
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

import requests
import json

# Register your models here.
class VimeoEmbed(object):
    def vimeo_embed(self, instance):
        url = 'https://player.vimeo.com/video/%s' % (instance.video_solution.vimeo_id)
        # url = 'https://player.vimeo.com/video/'+instance.vimeo_solution.vimeo_id
        if instance.pk:
            return mark_safe(u'<iframe frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen src={u}></iframe><script src="https://player.vimeo.com/api/player.js"></script>'.format(u=url))
        else:
            return ''

class DisplayLatex(object):
    def disply_latex(self, instance):
        text = '%s' % (instance.question.question_text)
        if instance.pk:
            return mark_safe(u'<div style="font-size: 22px; max-width: 60%;"class="latex">{u}</div>'.format(u=text))
        else:
            return ''
class ProblemInline(DisplayLatex, VimeoEmbed, SortableInlineAdminMixin, admin.StackedInline):
    model = Problem
    extra = 0
    # readonly_fields = ('vimeo_embed', 'disply_latex')

class MaturaAdmin(admin.ModelAdmin):
    model = Matura
    inlines = [
        ProblemInline,
    ]
    actions = ['update_problems',]
    list_editable = ('shopify_product_id',)

    @admin.action(description='Update product on Shopify')
    def update_problems(self, request, queryset):
        base_url = 'https://msandalj23.myshopify.com'
        headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': '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' }
        for matura in queryset:
            product_id = matura.shopify_product_id
            metafields_url = '/admin/products/{id}/metafields.json'.format(id=product_id)
            problems = Problem.objects.filter(matura=matura)
            serilizer = ProblemSerializer(problems, many=True)
            json_string = json.dumps(serilizer.data)
            metafield_data = {
                "metafield": {
                        "namespace": "matura",
                        "key": "zadatci_"+str(matura.term.term),
                        "value_type": "json_string",
                        "value": json_string,
                    }
                }
            url = base_url + metafields_url
            response = requests.post(url, headers=headers, json = metafield_data)
            print(response.json())
        
    list_display = ( '__str__' ,'created_at', 'shopify_product_id', 'subject')
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('subject',)

admin.site.register(Year)
admin.site.register(Term)
admin.site.register(Matura, MaturaAdmin)
admin.site.register(MaturaSubject)