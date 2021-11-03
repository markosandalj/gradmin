from django.contrib import admin

# Register your models here.
from .models import PDF, SVG, Image, Video

class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = ('name', 'vimeo_id',)
    search_fields = ('vimeo_id', 'name')

admin.site.register(Video, VideoAdmin)
admin.site.register(Image)
admin.site.register(SVG)
admin.site.register(PDF)