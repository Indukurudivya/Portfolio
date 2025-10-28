from django.shortcuts import render
from .models import  Skill, Project, Experience, About, Contact,Message
from django.http import FileResponse
from django.core.mail import send_mail
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
    con = Contact.objects.all()  # your static contact info

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # 1️⃣ Save message to database
            msg_obj = Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # 2️⃣ Send email
            full_message = f"""
            New message from your portfolio contact form:

            Name: {name}
            Email: {email}
            Subject: {subject}

            Message:
            {message}
            """

            send_mail(
                subject=f"New Contact Message: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],  # Your email
                fail_silently=False,
            )

            # 3️⃣ Show success page
           # return render(request, 'portfolio/contact_success.html', {'name': name})

    return render(request, 'portfolio/contact.html', {'contact': con})

def resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'Divya_Indukuru_Resume .pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

