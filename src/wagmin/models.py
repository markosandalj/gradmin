from django.db import models
from django.forms import Field

# WAGTAIL
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)

from course import blocks

# Create your models here.

class HomePage(Page):
    """Home page where user can choose between wagtail admin, django admin or custom made admin"""

    template = 'wagmin/home_page.html'
    max_count = 1

    page_title = models.CharField(max_length=100, blank=False, null=True)

    content = StreamField(
        [
            ('cards', blocks.HomePageCardBlock()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        StreamFieldPanel("content")
    ]

    class Meta:  # noqa
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"



class CoursePage(Page):
    """Course page"""

    # templates = 'course/course_page.html'
    max_count = 50

    course_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('course_title'),
        MultiFieldPanel(
            [
                InlinePanel("chapters", max_num=5, min_num=1, label="Lesson")
            ],
            heading="Chapters",
        )
    ]

    class Meta:
        verbose_name = "Course Page"
        verbose_name_plural = "Course Page"


class CourseChapter(Orderable):
    page = ParentalKey(CoursePage, related_name="chapters")
    chapter_title = models.CharField(max_length=100, blank=False, null=True)

    lessons = StreamField(
        [
            ('lesson_video', blocks.CourseLessonVideoBlock()),
            ('lesson_problem_solution', blocks.CourseLessonProblemSolutionBlock()),
            ('lesson_quiz', blocks.CourseLessonQuizBlock()),
            ('lesson_page_content', blocks.CourseLessonPageContentBlock()),
            ('lesson_interactive_map', blocks.CourseLessonInteractiveMapBlock()),
        ]
    )

    panels = [
        FieldPanel('chapter_title'),
        StreamFieldPanel('lessons'),
    ]