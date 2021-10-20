from django.db import models

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
    shopify_page_id = models.BigIntegerField(blank=True, null=True, unique=True)
    shopify_page_url = models.URLField(blank=True, null=True,)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    skripta = models.ManyToManyField('Skripta', blank=True, related_name='sections', through='SkriptaSection')
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    

    class Meta(object):
        ordering = ['order', ]
    
    def __str__(self):
        return str(self.name)

class Skripta(models.Model):
    name = models.TextField()

    subject = models.ForeignKey(
        Subject,
        blank=True,
        null=True, 
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return str(self.name)

class SkriptaSection(models.Model):
    skripta = models.ForeignKey(Skripta, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    section_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('section_order',)

class Equation(models.Model):
    name = models.TextField()
    equation = models.TextField()
    description = models.TextField(null=True, blank=True)
    related_equation = models.ManyToManyField('self')
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
    )

    def __str__(self):
        return str(self.name)