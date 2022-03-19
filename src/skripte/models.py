from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from media.models import PDF, SVG
# from problems.models import Problem

from shopify_models.models import Page

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return str(self.name)

class Section(models.Model):
    name = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True, related_name="subject_name", )
    skripta = models.ManyToManyField('Skripta', blank=True, related_name='sections', through='SkriptaSection')
    related_sections = models.ManyToManyField('self', blank=True, related_name='related_sections', through='SectionSection')
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey(
        'Category',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    icon = models.ForeignKey(
        SVG,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    exclude = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order', ]
    
    def __str__(self):
        return str(self.name)

class SectionSection(models.Model):
    main_section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='main_section')
    related_section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='related_section')
    related_section_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('related_section_order',)


class Skripta(models.Model):
    name = models.TextField()
    label = models.CharField(
        blank=True,
        null=True, 
        max_length=255
    )
    label_short = models.CharField(
        blank=True,
        null=True, 
        max_length=255
    )
    subject = models.ForeignKey(
        Subject,
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )
    file = models.ForeignKey(
        PDF,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order', ]

    def __str__(self):
        return str(self.name)

class SkriptaSection(models.Model):
    skripta = models.ForeignKey(Skripta, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    section_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('section_order',)

class ProblemEquation(models.Model):
    problem = ForeignKey('problems.Problem', on_delete=models.PROTECT)
    equation = ForeignKey('Equation', on_delete=models.PROTECT)
    equation_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('equation_order',)

class Equation(models.Model):
    name = models.TextField()
    equation = models.TextField()
    description = models.TextField(null=True, blank=True)
    related_equation = models.ManyToManyField('self', blank=True) 
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    subject = models.ForeignKey(
        Subject, 
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )
    section = models.ManyToManyField(
        Section, 
        blank=True,
        related_name='equations'
    )
    problem = models.ManyToManyField(
        'problems.Problem',
        blank=True,
        related_name='equations',
        through=ProblemEquation
    )

    def __str__(self):
        return str(self.name)

class Razred(models.Model):
    name = models.TextField()

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.TextField()
    razred = models.ForeignKey(
        Razred,         
        blank=True,
        null=True, 
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return str(self.name)

