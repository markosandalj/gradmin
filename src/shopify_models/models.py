from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Page(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('Active')
        HIDDEN = 'hidden', _('Hidden')
        
    page_id = models.BigIntegerField(blank=True, null=True, unique=True)
    title = models.TextField(blank=False, null=False)
    handle = models.CharField(max_length=255, blank=True, null=True, unique=True)
    seo_title = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    graphql_api_id = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=8, 
        blank=True, 
        null=True,
        choices=StatusChoices.choices,
        default=StatusChoices.HIDDEN
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    template = models.ForeignKey(
        'Template',
        blank=True, 
        null=True,
        on_delete=models.SET_NULL,
    )
    # template_sufix = models.CharField(max_length=500,blank=False, null=False, unique=True)
    # create template object that is gonna store all tempaltes so we can have dropdown picker 
    def __str__(self):
        return self.title

class Product(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('Active')
        ARCHIVED = 'archived', _('Archived')
        DRAFT = 'draft', _('Draft')
        
    product_id = models.BigIntegerField(blank=True, null=True, unique=True)
    title = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=8,
        blank=True, 
        null=True,
        choices=StatusChoices.choices
    )
    handle = models.CharField(max_length=255, blank=True, null=True, unique=True)
    graphql_api_id = models.TextField(blank=True, null=True)
    seo_title = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # dodati ManyToMany relaciju za tagove
    
    # template_sufix = models.CharField(max_length=500,blank=False, null=False, unique=True)
    # create 
    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.TextField(_("Collection title"))

class ProductTags(models.Model):
    text = models.TextField(_("Tag name"))

class Template(models.Model):
    template_suffix = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.template_suffix