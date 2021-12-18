from django.urls import path
from .views import AlpineView, IndexView

urlpatterns = [
    path('index', IndexView),
    path('index/skripta', IndexView),
    path('index/skripta/<str>', IndexView),
    path('index/skripta/<str>/<int>', IndexView),
    path('index/skripta/<str>/<int>/<i>', IndexView),
    path('index/matura/<int>/list', IndexView),
    path('index/matura/<int>', IndexView),
    path('alpine', AlpineView),
]
