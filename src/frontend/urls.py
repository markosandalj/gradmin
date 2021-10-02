from django.urls import path
from .views import IndexView

urlpatterns = [
    path('index', IndexView),
    path('index/skripta', IndexView),
    path('index/skripta/<str>', IndexView),
    path('index/skripta/<str>/<int>', IndexView),
    path('index/matura', IndexView),
    path('index/matura/<str>', IndexView),
    path('index/problems/fizika/matura/<int>', IndexView),
    path('index/problems/fizika/matura/<int>/print', IndexView),
    path('index/problems', IndexView),
]
