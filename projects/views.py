from datetime import date

from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import Project
from .pdfcreator import PdfCreator


def all_projects(request):

    projects = Project.objects.all()

    return render(request, 'projects.html', {'projects': projects,
                                             'current_year': date.today().year})


def show_project(request, project):

    projects = Project.objects.all()
    project = Project.objects.get(title=project)

    return render(request, 'project.html', {'projects': projects,
                                            'project': project,
                                            'current_year': date.today().year})

def download_project(request, project):
    import os
    path = 'DEBUG'

    import io
    from django.http import FileResponse

    output_path = settings.MEDIA_ROOT + 'pdf/%s.pdf' % project
    pure_html = str(show_project(request, project).content).replace('\\n', '')

    pdf = PdfCreator.create_pdf(pure_html, output_path)

    return FileResponse(open(output_path, 'rb'))
    return show_project(request, project)
