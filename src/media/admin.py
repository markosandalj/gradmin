from django.contrib import admin

# Register your models here.
from .models import PDF, SVG, Image, Video
import vimeo
import time
from django.contrib import messages
import requests
import json
from bs4 import BeautifulSoup

class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = ('name', 'vimeo_id',)
    search_fields = ('vimeo_id', 'name')
    actions = ['update_video_info',]

    @admin.action(description='Update videos info from Vimeo')
    def update_video_info(self, request, queryset):
        c = vimeo.VimeoClient(
                token='efe0a81055184db54700aa97ec9aa821',
                key='8e5f364f348c8c12ab10a8a3d48e35461a1e55fb',
                secret='zQHi4Z9WAalZ6LPUPP9lybCu5utepNl5mHtvL1QEnYpR/sgsKLFsC5Xvj/hMopJf9T0jJGfNHuWFTutePS7dGmZ8pRg1n3cVxf+RQOSRt0Kyf3eotVkWglaWmhX34UQn'
            )
        for video in queryset:
            if(video.vimeo_id != None):
                shuldSave = False
                try:
                    response = c.get("https://api.vimeo.com/me/videos/" + str(video.vimeo_id) )
                    data = response.json()
                    if(video.length == None):
                        duration = data['duration']
                        video.length = duration
                        shuldSave = True

                    secondary_id = data['link'].replace('https://vimeo.com/', '').split('/')[1]
                    if(video.vimeo_secondary_id == None or video.vimeo_secondary_id != secondary_id):
                        video.vimeo_secondary_id = secondary_id
                        shuldSave = True
                        
                    iframe = data['embed']['html']  
                    soup = BeautifulSoup(iframe, 'html.parser')
                    tag = soup.find_all('iframe')[0]
                    if(video.vimeo_embed_url == None or video.vimeo_embed_url != tag['src']):
                        video.vimeo_embed_url = tag['src']
                        shuldSave = True
                    if(video.vimeo_view_url == None or video.vimeo_view_url != data['link']):
                        video.vimeo_view_url = data['link']
                        shuldSave = True
                    if(video.vimeo_thumbnail_url == None or video.vimeo_thumbnail_url != data['pictures']['base_link']):
                        video.vimeo_thumbnail_url = data['pictures']['base_link']
                        shuldSave = True
                    
                    if(shuldSave):
                        video.save()
                        messages.success(request, "Video {u} ({v}) uspješno ažuriran.".format(v=data['name'], u = video.name ))

                    time.sleep(0.5)

                except:
                    print('Nes je krepalo:', video.vimeo_id)
                    messages.error(request, "No response. Zovi policiju!")


admin.site.register(Video, VideoAdmin)
admin.site.register(Image)
admin.site.register(SVG)
admin.site.register(PDF)