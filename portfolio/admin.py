from django.contrib import admin
from .models import PersonalInfo, Skill, Project, Experience, About

admin.site.register(PersonalInfo)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(About)
