from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
from .models import Subject, Section, Equation, Skripta

class SectionInline(admin.StackedInline):
    model = Section.skripta.through
    extra = 0

class SkriptaAdmin(admin.ModelAdmin):
    model = Skripta
    list_filter = ('subject',)
    list_display = ('name','id', )
    

    inlines = [
        SectionInline,
    ]

class SectionAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Section
    list_display = ('name','shopify_page_id', )
    list_filter = ('subject',)
    readonly_fields = ('created_at', 'updated_at',)


admin.site.register(Equation)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subject)
admin.site.register(Skripta, SkriptaAdmin)