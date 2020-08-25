from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.all_projects, name='projects'),
    path('/<str:project>', views.show_project),
    path('/download/<str:project>', views.download_project),
]
