"""Course stream fields"""

from numpy import require
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

class CourseLessonInteractiveMapBlock(blocks.StructBlock):
    """Course lesson that displays content of selected interactive map"""
    
    # shuold have foreign key to InteractiveMap model 
    #   -> we will want to reuse those maps in multiple courses
    # should have edit link to that model

    title=blocks.CharBlock(required=True, help_text="Title that will be displayed on web")
    admin_title=blocks.CharBlock(required=True, help_text="Title that will be displayed only in admin")

    lessons = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.TextBlock(required=True, max_length=100))
            ]
        )
    )

    class Meta:  # noqa
        icon = "uni52"
        label = "Course lesson - interactive map"
        min_num = 0

class CourseLessonPageContentBlock(blocks.StructBlock):
    """Course lesson that displays content of selected page"""

    # should have foreign key to ShopifyPage model
    #   -> we will want to reuse those models
    #   -> that model should at some point be converted to Wagtail page
    # should have edit link to that model

    title=blocks.CharBlock(required=True, help_text="Title that will be displayed on web")
    admin_title=blocks.CharBlock(required=True, help_text="Title that will be displayed only in admin")

    lessons = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.TextBlock(required=True, max_length=100))
            ]
        )
    )

    class Meta:  # noqa
        icon = "doc-full"
        label = "Course lesson - page content"
        min_num = 0


class CourseLessonVideoBlock(blocks.StructBlock):
    """Course lesson that displays problem soltion"""

    # should have foreign key to Video model
    #   -> we will want to reuse that video in multiple courses
    # should have edit link to that model

    title=blocks.CharBlock(required=True, help_text="Title that will be displayed on web")
    admin_title=blocks.CharBlock(required=True, help_text="Title that will be displayed only in admin")

    lessons = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.TextBlock(required=True, max_length=100))
            ]
        )
    )

    class Meta:  # noqa
        icon = "media"
        label = "Course lesson - video + text"
        min_num = 0


class CourseLessonQuizBlock(blocks.StructBlock):
    """Course lesson that displays quiz with problems"""

    # should have foreign key to Quiz model
    #   -> we will want to reuse that quiz in multiple courses/pages
    # should have edit link to that model

    title=blocks.CharBlock(required=True, help_text="Title that will be displayed on web")
    admin_title=blocks.CharBlock(required=True, help_text="Title that will be displayed only in admin")

    lessons = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.TextBlock(required=True, max_length=100))
            ]
        )
    )

    class Meta:  # noqa
        icon = "tasks"
        label = "Course lesson - quiz"
        min_num = 0

class CourseLessonProblemSolutionBlock(blocks.StructBlock):
    """Course lesson that displays problem solution"""

    # should have foreign key to Problem model
    #   -> we will want to reuse that problem wherever
    # should have edit link to that model

    title=blocks.CharBlock(required=True, help_text="Title that will be displayed on web")
    admin_title=blocks.CharBlock(required=True, help_text="Title that will be displayed only in admin")

    lessons = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.TextBlock(required=True, max_length=100))
            ]
        )
    )

    class Meta:  # noqa
        icon = "placeholder"
        label = "Course lesson - problem solution"
        min_num = 0



class HomePageCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required = True)

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required = True)),
                ('link', blocks.CharBlock(required = True))
            ]
        )
    )