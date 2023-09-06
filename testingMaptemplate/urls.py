from django.urls import path
from . import views

urlpatterns = [
    path('', views.MapPage, name='foodmapstore'),
]
