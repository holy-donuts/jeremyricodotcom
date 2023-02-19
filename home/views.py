from django.shortcuts import render
from .models import Project, Position, Education, Skill

def home(request):
    positions = Position.objects.all()
    projects = Project.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()

    context = {
      'positions': positions,
      'projects':projects,
      'educations': educations,
      'skills': skills,
    }
    return render(request, 'home.html', context)
