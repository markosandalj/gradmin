from django.contrib import admin
from django.db.models.fields import IntegerField
from django.db.models.functions.comparison import Cast
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.db.models.base import Model
from django.contrib import messages
from django.utils.translation import ngettext
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.admin import SimpleListFilter
# from django_reverse_admin import ReverseModelAdmin

# Register your models here.
from media.models import Image
from skripte.models import Equation
from mature.models import Matura
from .models import Question
from .models import AnswerChoice
from .models import CorrectAnswer
from .models import Hint
from .models import Problem
from skripte.admin import ProblemEquationInline


class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}" target="_blank">Edit</a>'.format(u=url))
        else:
            return ''

# QUESTIONS
class FilterQuestionsByMatura(SimpleListFilter):
    title = 'Questions by matura'
    parameter_name = 'by_matura'

    def lookups(self, request, model_admin):
        filter_list = [ (str(matura.id), _(str(matura)) ) for matura in Matura.objects.all() ]
        print(filter_list)
        return filter_list

    def queryset(self, request, queryset): 
        if self.value():
            problems = Problem.objects.filter(matura__id = self.value())
            questions_list = [ problem.question.id for problem in problems]
            return queryset.filter( id__in = questions_list)

class QuestionInline(EditLinkToInlineObject, admin.StackedInline):
    model = Question
    extra=0
    readonly_fields = ('edit_link',)
    

class AnswerChoiceInline(EditLinkToInlineObject, SortableInlineAdminMixin, admin.StackedInline):
    model = AnswerChoice
    extra=0
    readonly_fields = ('edit_link', 'id')

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
    list_filter = (FilterQuestionsByMatura,)
    list_display = ('question_number', 'question_text')
    readonly_fields = ('created_at', 'updated_at',)

    def question_number(self, obj):
        return obj.question_text.split(' ')[0] + " zadatak"

class AnswerChoiceAdmin(admin.ModelAdmin):
    model = AnswerChoice
    search_fields = ('choice_text', 'id')
    list_display = ('id', 'choice_text',)
    inlines = [
        ImageInline
    ]

# PROBLEMS
class EmptyAnswerFilter(SimpleListFilter):
    title = 'empty answer' # or use _('country') for translated title
    parameter_name = 'empty_answer'

    def lookups(self, request, model_admin):
        return [ 
            ('no_answer', _('No answer')),
            ('has_answer', _('Has answer')),
            ]

    def queryset(self, request, queryset):
        answer_question_ids = [ans.question.id for ans in CorrectAnswer.objects.all()]
        no_ans_queryset = queryset.exclude(question__id__in = answer_question_ids)
        has_ans_queryset = queryset.filter(question__id__in = answer_question_ids)
        if self.value() == 'no_answer':
            return no_ans_queryset
        elif self.value() == 'has_answer':
            return has_ans_queryset
        elif self.value():
            return queryset

class EmptySectionFilter(SimpleListFilter):
    title = 'empty section' # or use _('country') for translated title
    parameter_name = 'empty_section'

    def lookups(self, request, model_admin):
        return [ 
            ('no_section', _('No section')),
            ]

    def queryset(self, request, queryset):
        if self.value() == 'no_section':
            return queryset.filter(section=None)
        elif self.value():
            return queryset

class ProblemAdmin(admin.ModelAdmin):
    model = Problem
    list_display = ('name', 'shop_availability', 'approval', 'section' )
    list_filter = ('subject', 'matura','shop_availability', 'approval', EmptyAnswerFilter, EmptySectionFilter)
    list_editable = ('shop_availability','approval', 'section')
    search_fields = ('name', 'question__question_text', 'section__name',)
    autocomplete_fields = ('matura', 'question',)
    actions = ['make_available', 'make_unavailable', 'make_hidden', 'approve', 'unapprove',]
    inlines = [
        ProblemEquationInline
    ]

    @admin.action(description='Approve selected items')
    def approve(self, request, queryset):
        updated = queryset.update(approval='approved')
        self.message_user(request, ngettext(
            '%d problem was successfully marked as approved.',
            '%d problem were successfully marked as approved.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Unapprove selected items')
    def unapprove(self, request, queryset):
        updated = queryset.update(approval='unapproved')
        self.message_user(request, ngettext(
            '%d problem was successfully marked as unapproved.',
            '%d problem were successfully marked as unapproved.',
            updated,
        ) % updated, messages.SUCCESS)

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
            '%d problems were successfully marked as hidden.',
            updated,
        ) % updated, messages.SUCCESS)

    readonly_fields = ('created_at', 'updated_at',)

class CorrectAnswersAdmin(admin.ModelAdmin):
    model = CorrectAnswer
    list_display = ('id', 'answer_text', 'answer_choice', 'question','created_at',)
    search_fields = ('question__question_text','id', 'answer_text', 'answer_choice__choice_text') 
    readonly_fields = ('created_at', 'updated_at',)
    autocomplete_fields = ('answer_choice',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerChoice, AnswerChoiceAdmin)
admin.site.register(CorrectAnswer, CorrectAnswersAdmin)
admin.site.register(Hint)
admin.site.register(Problem, ProblemAdmin)


