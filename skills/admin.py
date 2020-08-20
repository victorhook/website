from django.contrib import admin

# Register your models here.

from .models import SkillCategory, Skill

admin.site.register(SkillCategory)
admin.site.register(Skill)
