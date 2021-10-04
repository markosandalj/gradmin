from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.db.models.base import Model
from django.contrib import messages
from django.utils.translation import ngettext
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
from mature.models import Year, Term, Matura, MaturaSubject
from media.models import Image, Video
from skripte.models import Subject, Section, Equation, Skripta
from .models import Question
from .models import AnswerChoice
from .models import CorrectAnswer
from .models import Hint
from .models import Problem

class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}" target="_blank">Edit</a>'.format(u=url))
        else:
            return ''

# QUESTIONS
class QuestionInline(EditLinkToInlineObject, admin.StackedInline):
    model = Question
    extra=0
    readonly_fields = ('edit_link', )

class AnswerChoiceInline(EditLinkToInlineObject, SortableInlineAdminMixin, admin.StackedInline):
    model = AnswerChoice
    extra=0
    readonly_fields = ('edit_link', )

class CorrectAnswerInline(EditLinkToInlineObject, admin.StackedInline):
    model = CorrectAnswer
    autocomplete_fields = ('answer_choice',)
    extra=0
    readonly_fields = ('edit_link', )

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [
        CorrectAnswerInline,
        AnswerChoiceInline,
        QuestionInline,
        ImageInline,
    ]
    search_fields = ('id', 'question_text',)
    list_display = ('id', 'question_text', )
    readonly_fields = ('created_at', 'updated_at',)

class AnswerChoiceAdmin(admin.ModelAdmin):
    model = AnswerChoice
    search_fields = ('choice_text', 'id')
    inlines = [
        ImageInline
    ]

# PROBLEMS
class ProblemAdmin(admin.ModelAdmin):
    model = Problem
    list_display = ('name', 'question', 'shop_availability', 'matura', 'subject',)
    list_filter = ('shop_availability', 'subject', 'matura',)
    list_editable = ('shop_availability',)
    search_fields = ('name', 'question', 'section',)
    actions = ['make_available', 'make_unavailable', 'make_hidden']

    @admin.action(description='Make selected items available')
    def make_available(self, request, queryset):
        updated = queryset.update(shop_availability='available')
        self.message_user(request, ngettext(
            '%d problem was successfully marked as available.',
            '%d problem were successfully marked as available.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Make selected items unavailable')
    def make_unavailable(self, request, queryset):
        updated = queryset.update(shop_availability='unavailable')
        self.message_user(request, ngettext(
            '%d problem was successfully marked as unavailable.',
            '%d problem were successfully marked as unavailable.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Make selected items hidden')
    def make_hidden(self, request, queryset):
        updated = queryset.update(shop_availability='hidden')
        self.message_user(request, ngettext(
            '%d problem was successfully marked as hidden.',
            '%d problem were successfully marked as hidden.',
            updated,
        ) % updated, messages.SUCCESS)
    readonly_fields = ('created_at', 'updated_at',)

class CorrectAnswersAdmin(admin.ModelAdmin):
    model = CorrectAnswer
    list_display = ('answer_text', 'answer_choice', 'question','created_at',)
    search_fields = ('question__question_text',)
    readonly_fields = ('created_at', 'updated_at',)
    autocomplete_fields = ('answer_choice',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerChoice, AnswerChoiceAdmin)
admin.site.register(CorrectAnswer, CorrectAnswersAdmin)
admin.site.register(Hint)
admin.site.register(Problem, ProblemAdmin)


