from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.TextField(blank=False, null=False)
    seo_description = models.TextField(blank=True, null=True)
    seo_title = models.TextField(blank=True, null=True)
    page_id = models.IntegerField(blank=True, null=True)



class Product(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=False, null=False)
    seo_description = models.TextField(blank=True, null=True)
    seo_title = models.TextField(blank=True, null=True)

