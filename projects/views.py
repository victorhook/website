from datetime import date
import re

from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings

from .models import Project
from .pdfcreator import PdfCreator

IMAGES = '/static/images'


def all_projects(request):
    projects = Project.objects.all()
    for project in projects:
        project.image_url = IMAGES + project.image.url

    return render(request, 'projects.html', {'projects': projects,
                                             'current_year': date.today().year})


def inject_a_tag(project):
    """ Replaces LINK[url](name) with an html a-tag. """
    links = re.findall('LINK\[.*?\]', project.body)
    link_names = re.findall('LINK\[.*?\]\(.*?\)', project.body)

    for link, whole_link in zip(links, link_names):
        url = link.split('LINK[')[1][:-1]
        name = whole_link[len(link):][1:-1]

        new_tag = f'<a href="{url}">{name}</a>'
        project.body = project.body.replace(whole_link, new_tag)

    return project

def show_project(request, project):
    projects = Project.objects.all()
    project = Project.objects.get(title=project)

    # Objectives and lessons learned from the project are represented as
    # a string, where \n means a new entity.
    project.experiences = project.learned.split('\n')
    project.objectives = project.objective.split('\n')
    project.image_url = IMAGES + project.image.url

    project = inject_a_tag(project)

    return render(request, 'project.html', {'projects': projects,
                                            'project': project,
                                            'current_year': date.today().year})

def download_project(request, project):

    output_path = settings._STATIC_ROOT + f'/pdf/{project.title}.pdf'
    # re.sub didn't work here for some reason, so have to use replace() instead
    pure_html = str(show_project(request, project).content).replace('\\n', '')
    pure_html = pure_html.replace('\\r', '').replace("\\'", "'")

    pdf = PdfCreator.create_pdf(pure_html,
                                request.build_absolute_uri(),
                                '/css/projects.css',
                                output_path)
    try:
        return FileResponse(open(output_path, 'rb'))
    except FileNotFoundError:
        return show_project(request, project)

