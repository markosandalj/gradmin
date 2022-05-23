from django.contrib import admin

# Register your models here.
from .models import Course, CourseLesson, CourseChapter, CourseQuizz, CourseStepByStepProblem, CourseProblemVideo
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline
# from merged_inlines.admin import MergedInlineAdmin
from problems.admin import EditLinkToInlineObject



class CourseChapterInline(SortableInlineAdminMixin, EditLinkToInlineObject, admin.StackedInline):
    model = CourseChapter
    extra = 0

class CourseLessonInline(StackedPolymorphicInline):

    class CourseQuizzInline(StackedPolymorphicInline.Child):
        model = CourseQuizz

    class CourseProblemVideoInline(StackedPolymorphicInline.Child):
        model = CourseProblemVideo
    
    class CourseStepByStepProblemInline(StackedPolymorphicInline.Child):
        model = CourseStepByStepProblem

    model = CourseLesson
    extra = 0
    child_inlines = (
        CourseQuizzInline,
        CourseProblemVideoInline,
        CourseStepByStepProblemInline
    )

class CourseChapterAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    model = CourseChapter
    inlines = [
        CourseLessonInline,
    ]  

class CourseAdmin(admin.ModelAdmin):
    model = Course
    inlines = [
        CourseChapterInline,
    ]



admin.site.register(Course, CourseAdmin)
admin.site.register(CourseChapter, CourseChapterAdmin)
admin.site.register(CourseLesson)
admin.site.register(CourseProblemVideo)
admin.site.register(CourseQuizz)
admin.site.register(CourseStepByStepProblem)
