import sys
from django.contrib import admin

# Register your models here.
from .models import PDF, SVG, Image, Video
import vimeo
import time
from django.contrib import messages
import requests
import json
from bs4 import BeautifulSoup
from django.conf import settings

class ImageAdmin(admin.ModelAdmin):
    model = Image
    autocomplete_fields = ('question',)

class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = ('name', 'vimeo_id',)
    search_fields = ('vimeo_id', 'name')
    actions = ['update_video_info',]

    @admin.action(description='Update videos info from Vimeo')
    def update_video_info(self, request, queryset):
        c = vimeo.VimeoClient(
                token=settings.VIMEO_TOKEN,
                key=settings.VIMEO_KEY,
                secret=settings.VIMEO_SECRET
            )
        for video in queryset:
            if(video.vimeo_id != None):
                shuldSave = False
                actions = ''
                try:
                    response = c.get("https://api.vimeo.com/me/videos/" + str(video.vimeo_id) )
                    data = response.json()
                    if(video.length == None):
                        duration = data['duration']
                        video.length = duration
                        shuldSave = True
                        actions += 'duration, '

                    secondary_id = data['link'].replace('https://vimeo.com/', '').split('/')[1]
                    if(video.vimeo_secondary_id == None or video.vimeo_secondary_id != secondary_id):
                        video.vimeo_secondary_id = secondary_id
                        shuldSave = True
                        actions += 'secondary id, '
                        
                    iframe = data['embed']['html']  
                    soup = BeautifulSoup(iframe, 'html.parser')
                    tag = soup.find_all('iframe')[0]
                    if(video.vimeo_embed_url == None or video.vimeo_embed_url != tag['src']):
                        video.vimeo_embed_url = tag['src']
                        shuldSave = True
                        actions += 'embed url, '
                    if(video.vimeo_view_url == None or video.vimeo_view_url != data['link']):
                        video.vimeo_view_url = data['link']
                        shuldSave = True
                        actions += 'view url, '
                    if(video.vimeo_thumbnail_url == None or video.vimeo_thumbnail_url != data['pictures']['base_link']):
                        video.vimeo_thumbnail_url = data['pictures']['base_link']
                        shuldSave = True
                        actions += 'thumbnail url, '
                    
                    if(shuldSave):
                        video.save()
                        messages.success(request, "Video {u} ({v}) uspješno ažuriran. ({a})".format(v=data['name'], u = video.name, a = actions ))
                    else:
                        messages.info(request, "Video {u} već ima točno unesene podatke.".format(u = video.name))

                    time.sleep(0.5)

                except:
                    print('Nes je krepalo:', video.vimeo_id, sys.exc_info()[0])
                    messages.error(request, "No response. Zovi policiju!")


admin.site.register(Video, VideoAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(SVG)
admin.site.register(PDF)