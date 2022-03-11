from django.urls import path

from . import views

urlpatterns = [
    path('', views.photography, name='photography'),
    path('photo', views.photo, name='photo'),
]
