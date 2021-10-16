from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Page(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('Active')
        ARCHIVED = 'archived', _('Archived')
        DRAFT = 'draft', _('Draft')
        
    page_id = models.BigIntegerField(blank=True, null=True, unique=True)
    title = models.TextField(blank=False, null=False)
    handle = models.CharField(max_length=255, blank=False, null=False, unique=True)
    seo_title = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    product_type = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=8, 
        blank=False, 
        null=False,
        choices=StatusChoices.choices
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    # template_sufix = models.CharField(max_length=500,blank=False, null=False, unique=True)
    # create template object that is gonna store all tempaltes so we can have dropdown picker 


class Product(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('Active')
        ARCHIVED = 'archived', _('Archived')
        DRAFT = 'draft', _('Draft')
        
    product_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=False, null=False)
    seo_title = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    product_type = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=8, 
        blank=False, 
        null=False,
        choices=StatusChoices.choices
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    # template_sufix = models.CharField(max_length=500,blank=False, null=False, unique=True)
    # create 

