from django.urls import path
from .views import problems_list_view

urlpatterns = [
    path('list/', problems_list_view),
]
