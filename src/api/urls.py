from django.urls import path

from .views import MaturaListApiView, MaturaProblemsApiView, SkriptaApiView, SkriptaSectionProblemsApiView, SkriptaSectionsApiView, UpdateQuestionApiView

urlpatterns = [
    # path('maturas/', MaturaWithoutProblemsApiView.as_view()),
    # path('maturas/<int:pk>', MaturaApiView.as_view()),
    # path('maturas/<str:subject__name>', MaturaWithoutProblemsApiView.as_view()),
    # path('maturas/<str:subject__name>/<str:year__year>', MaturaWithoutProblemsApiView.as_view()),
    # path('maturas/<str:subject__name>/<str:year__year>/<str:term__term>', MaturaWithoutProblemsApiView.as_view()),
    path('question/update', UpdateQuestionApiView.as_view()),
    path('skripta/<int:skripta_id>/list', SkriptaSectionsApiView.as_view()),
    path('skripta/<int:pk>', SkriptaApiView.as_view()),
    path('skripta/<int:skripta_id>/<int:section_id>', SkriptaSectionProblemsApiView.as_view()),
    path('matura/<int:matura_id>', MaturaProblemsApiView.as_view()),
    path('matura/<int:subject_id>/list', MaturaListApiView.as_view())
]