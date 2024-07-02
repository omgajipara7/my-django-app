from django.contrib import admin

# Register your models here.

# Portfolio/admin.py
from django.contrib import admin
from .models import Project, Skill, Tool

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tool)
