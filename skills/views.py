from django.shortcuts import render

from datetime import date

from .models import SkillCategory, Skill

def skills(request):

    skill_categories = {}
    for skill in Skill.objects.all():
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)

    return render(request, 'skills.html', {'skill_categories': skill_categories,
                                           'current_year': date.today().year})
