from django.contrib import admin
from django.contrib import messages
from django.db.models.fields import IntegerField
from django.db.models.functions.comparison import Cast

from mature.models import Matura, MaturaSubject, Term, Year
from media.models import Video
from problems.admin import EditLinkToInlineObject
from problems.models import Problem, Question
from django.urls import reverse
from django.utils.safestring import mark_safe
from api.serializers import ProblemSerializer
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
import vimeo

import requests
import json
from bs4 import BeautifulSoup

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
            
class MaturaProblemInline(EditLinkToInlineObject, admin.StackedInline):
    model = Problem
    extra = 0
    # search_fields = ('section', 'skripta',)
    autocomplete_fields = ('section', 'skripta', 'question',)
    ordering = [Cast('number', IntegerField() ),]
    exclude = ('order',)
    # readonly_fields = ('question', )

class MaturaAdmin(admin.ModelAdmin):
    model = Matura
    inlines = [
        MaturaProblemInline,
    ]
    search_fields = ('name',)
    actions = ['update_problems', 'import_videos',]
    # list_editable = ('shopify_product_id',)

    @admin.action(description='Import videos from Vimeo')
    def import_videos(self, request, queryset):
        c = vimeo.VimeoClient(
                token='efe0a81055184db54700aa97ec9aa821',
                key='8e5f364f348c8c12ab10a8a3d48e35461a1e55fb',
                secret='zQHi4Z9WAalZ6LPUPP9lybCu5utepNl5mHtvL1QEnYpR/sgsKLFsC5Xvj/hMopJf9T0jJGfNHuWFTutePS7dGmZ8pRg1n3cVxf+RQOSRt0Kyf3eotVkWglaWmhX34UQn'
            )
        for matura in queryset:
            id = matura.vimeo_folder_id
            try:
                response = c.get("https://api.vimeo.com/me/projects/"+str(id)+"/videos?per_page=100")
                data = response.json()['data']
                problems = Problem.objects.annotate(number_field=Cast('number', IntegerField())).filter(matura=matura)
                if(len(data) == len(problems)):
                    for item, problem in zip(reversed(data), problems):
                        print(item['name'], problem.name, item['link'].replace('https://vimeo.com/', '').split('/')[1])
                        iframe = item['embed']['html']  
                        soup = BeautifulSoup(iframe, 'html.parser')
                        tag = soup.find_all('iframe')[0]
                        if(problem.video_solution):
                            video = problem.video_solution
                            video.name=problem.name
                            video.vimeo_id=int(item['uri'].replace('/videos/', ''))
                            video.vimeo_secondary_id=item['link'].replace('https://vimeo.com/', '').split('/')[1]
                            video.vimeo_view_url=item['link']
                            video.vimeo_embed_url=tag['src']
                            video.save()
                            messages.success(request, "Video {v} uspješno ažuriran".format(v=item['name']))
                        else:
                            new_video_solution = Video(
                                name=problem.name,
                                vimeo_id=int(item['uri'].replace('/videos/', '')),
                                vimeo_secondary_id=item['link'].replace('https://vimeo.com/', '').split('/')[1],
                                vimeo_view_url=item['link'],
                                vimeo_embed_url=tag['src'],
                            )
                            new_video_solution.save()
                            problem.video_solution = new_video_solution
                            problem.save()
                            messages.success(request, "Video {v} uspješno dodan u bazu i pod problem {p}".format(v=item['name'], p=problem.name))
                else:
                    messages.error(request, "Broj zadataka u bazi je razlicit od broja videa u folderu")
            except:
                messages.error(request, "No response. Zovi policiju!")

    

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