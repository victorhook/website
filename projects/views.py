from datetime import date

from django.shortcuts import render

from .models import Project

def all_projects(request):

    projects = Project.objects.all()

    return render(request, 'projects.html', {'projects': projects,
                                             'current_year': date.today().year})


def project(request, project):

    projects = Project.objects.all()
    project = Project.objects.get(title=project)

    return render(request, 'project.html', {'projects': projects,
                                            'project': project,
                                            'current_year': date.today().year})
