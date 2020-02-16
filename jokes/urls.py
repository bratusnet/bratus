from django.urls import path

from .import views

urlpatterns = [
    path('joke', views.joke, name='joke')
]