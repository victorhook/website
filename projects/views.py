from datetime import date

from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings

from .models import Project
from .pdfcreator import PdfCreator


def all_projects(request):

    projects = Project.objects.all()

    return render(request, 'projects.html', {'projects': projects,
                                             'current_year': date.today().year})


def show_project(request, project):
    IMAGES = '/static/images'

    projects = Project.objects.all()
    project = Project.objects.get(title=project)

    # Objectives and lessons learned from the project are represented as
    # a string, where \n means a new entity.
    project.experiences = project.learned.split('\n')
    project.objectives = project.objective.split('\n')
    project.image_url = IMAGES + project.image.url

    return render(request, 'project.html', {'projects': projects,
                                            'project': project,
                                            'current_year': date.today().year})

def download_project(request, project):
    output_path = settings.STATIC_ROOT + f'/pdf/{project}.pdf'
    # re.sub didn't work here for some reason, so have to use replace() instead
    pure_html = str(show_project(request, project).content).replace('\\n', '')
    pure_html = pure_html.replace('\\r', '').replace("\\'", "'")

    pdf = PdfCreator.create_pdf(pure_html,
                                request.build_absolute_uri(),
                                '/css/projects.css',
                                output_path)
    try:
        return FileResponse(open(output_path, 'rb'))
    except FileNotFoundException:
        return show_project(request, project)

