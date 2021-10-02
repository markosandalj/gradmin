from django.contrib import admin

from mature.models import Matura, MaturaSubject, Term, Year
from problems.models import Problem

# Register your models here.

class ProblemInline(admin.StackedInline):
    model = Problem
    extra = 0

class MaturaAdmin(admin.ModelAdmin):
    model = Matura
    inlines = [
        ProblemInline,
    ]
    list_display = ( '__str__' ,'created_at', 'subject')
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('subject',)

admin.site.register(Year)
admin.site.register(Term)
admin.site.register(Matura, MaturaAdmin)
admin.site.register(MaturaSubject)