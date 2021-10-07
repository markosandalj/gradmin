from django.db import models
from datetime import datetime
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.core.files.storage import FileSystemStorage

from django.db.models.deletion import CASCADE, PROTECT


# related models from other apps
from mature.models import Matura
from media.models import Video
from skripte.models import Section, Subject, Skripta


# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    main_question = models.ForeignKey("self", blank=True, null=True,on_delete=models.CASCADE,related_name='subquestions')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        ordering = ['order',]

    def __str__(self):
        return str(self.question_text)

class AnswerChoice(models.Model):
    choice_text = models.TextField()
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        related_name='answer_choices'
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        ordering = ['order',]

    def __str__(self):
        return str(self.choice_text)

class CorrectAnswer(models.Model):
    answer_text = models.TextField(blank=True, null=True, )
    answer_choice = models.ForeignKey(
        AnswerChoice,
        blank=True, 
        null=True, 
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        Question,
        blank=True, 
        null=True, 
        on_delete=models.CASCADE,
        related_name='correct_answer',
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        answer_label = str(self.answer_text) if self.answer_text else str(self.answer_choice)
        return str(answer_label)


class Problem(models.Model):
    class Availability(models.TextChoices):
        AVAILABILABE = 'available', _('Available')
        UNAVAILABLE = 'unavailable', _('Unavailable')
        HIDDEN = 'hidden', _('Hidden')
    class Approval(models.TextChoices):
        APPROVED = 'approved', _('Approved')
        UNAPPROVED = 'unapproved', _('Unapproved')

    name = models.TextField()
    number = models.CharField(
        max_length=5 ,
        blank=True,
        null=True, 
    )
    approval = models.CharField(
        max_length=20, 
        choices=Approval.choices, 
        default=Approval.UNAPPROVED,
    )
    shop_availability = models.CharField(
        max_length=20, 
        choices=Availability.choices, 
        default=Availability.HIDDEN,
        help_text='Hidden = problem wont be shown anywhere, Available = it is going to br shown as free preview, Unavailable = wont be shown as a free preivew. Only when bought.'
    )
    matura = models.ForeignKey(
        Matura, 
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
        related_name='problems'
    )
    question = models.ForeignKey(
        Question, 
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )
    subject = models.ForeignKey(
        Subject, 
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )
    section = models.ForeignKey(
        Section, 
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
        related_name='problems',
    )
    video_solution = models.ForeignKey(
        Video,
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )
    skripta = models.ManyToManyField(Skripta, blank=True,related_name='problems')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        ordering = ['question', 'number',]
        

    def __str__(self):
        return str(self.name)

class Hint(models.Model):
    text = models.TextField(null=True, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.problem)




