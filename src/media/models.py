# Create your models here.
from django.db import models
from django.core.validators import FileExtensionValidator


# from problems.models import AnswerChoice, Question

# Create your models here.

class Image(models.Model):
    image = models.ImageField(null=True, blank=True)
    image_dark = models.ImageField(null=True, blank=True)
    question = models.ForeignKey(
        'problems.Question', 
        blank=True,
        null=True, 
        on_delete=models.CASCADE,
        related_name='images'
    )
    answer_choice = models.ForeignKey(
        'problems.AnswerChoice',
        blank=True, 
        null=True, 
        on_delete=models.CASCADE,
        related_name='images'
    )
    correct_answer = models.ForeignKey(
        'problems.CorrectAnswer',
        blank=True, 
        null=True, 
        on_delete=models.CASCADE,
        related_name='images'
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order',]


class Video(models.Model):
    name = models.TextField(blank=True,null=True,)
    length = models.BigIntegerField(blank=True,null=True,)
    vimeo_id = models.IntegerField(blank=True,null=True,)
    vimeo_secondary_id = models.CharField(max_length = 200, blank=True,null=True,)
    vimeo_view_url = models.URLField(max_length = 1000, blank=True,null=True,)
    vimeo_embed_url = models.URLField(max_length = 1000, blank=True,null=True,)
    vimeo_thumbnail_url = models.URLField(max_length = 1000, blank=True,null=True,)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)

class SVG(models.Model):
    name = models.TextField(blank=True,null=True,)
    image = models.FileField(upload_to="svg/", validators=[FileExtensionValidator(['svg'])])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)

class PDF(models.Model):
    name = models.TextField(blank=True,null=True,)
    file = models.FileField(upload_to="pdf/", validators=[FileExtensionValidator(['pdf'])])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.name)