from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from model_utils.managers import InheritanceManager
from polymorphic.models import PolymorphicModel
from polymorphic.managers import PolymorphicManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Course(models.Model):
    title = models.TextField()
    shopify_product = models.ForeignKey('shopify_models.Product', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class CourseChapter(models.Model):
    title = models.TextField()
    course = models.ForeignKey("courses.Course", null=True, blank=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order', ]


    def __str__(self):
        return self.title

class CourseLesson(PolymorphicModel):
    title = models.TextField()
    chapter = models.ForeignKey(CourseChapter, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    # availability = 
    objects = PolymorphicManager()

    class Meta(object):
        ordering = ['order', ]

    def __str__(self):
        return self.title

class CourseQuizz(CourseLesson):
    description = models.TextField()

class CourseProblemVideo(CourseLesson):
    description = models.TextField()
    rich_text = RichTextUploadingField(null=True, blank=True,config_name="default",)
    problem = models.ForeignKey("problems.Problem", on_delete=models.CASCADE)

class CourseStepByStepProblem(CourseLesson):
    problem = models.ForeignKey("problems.Problem", on_delete=models.CASCADE)


