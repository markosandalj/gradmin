from atexit import register
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register your models here.
from .models import Cheatsheet, CheatsheetSeactionEquation, CheatsheetSection, CheatsheetTableEquation, CheatsheetTable, CheatsheetLayout
from skripte.models import Equation


class CheatsheetSectionEquationInline(SortableInlineAdminMixin, admin.TabularInline):
    model = CheatsheetSeactionEquation
    autocomplete_fields = ('equation',)
    extra = 0

class CheatsheetSectionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = CheatsheetSection
    extra = 0

class CheatsheetTableEquationInline(SortableInlineAdminMixin, admin.TabularInline):
    model = CheatsheetTableEquation
    autocomplete_fields = ('equation',)
    extra = 0

class CheatsheetSectionAdmin(admin.ModelAdmin):
    model = CheatsheetSection
    inlines = [
        CheatsheetSectionEquationInline
    ]
class CheatsheetTableAdmin(admin.ModelAdmin):
    model = CheatsheetTable
    inlines = [
        CheatsheetTableEquationInline
    ]

class CheatsheetAdmin(admin.ModelAdmin):
    model = Cheatsheet
    inlines = [
        CheatsheetSectionInline
    ]

admin.site.register(Cheatsheet, CheatsheetAdmin)
admin.site.register(CheatsheetSection, CheatsheetSectionAdmin)
admin.site.register(CheatsheetTable, CheatsheetTableAdmin)
admin.site.register(CheatsheetLayout)
