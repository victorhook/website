from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_projects, name='projects'),
    path('/<str:project>', views.project)
]
