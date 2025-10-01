from django.shortcuts import render
from .models import PersonalInfo, Skill, Project, Experience, About, Contact
from django.http import FileResponse
from django.conf import settings
import os

def home(request):
    return render(request, 'portfolio/home.html')

def about_view(request):
    about = About.objects.first()  
    return render(request, 'portfolio/about.html', {'about': about})

def skills(request):
    all_skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': all_skills})

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})

def experience(request):
    all_exp = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {'experience': all_exp})

def contact(request):
    con = Contact.objects.all()
    return render(request, 'portfolio/contact.html', {'contact': con})

def resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'Divya_Indukuru_Resume .pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

