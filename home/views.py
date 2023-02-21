from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .models import Project, Position, Education, Skill
from .forms import ContactForm

def home(request):
    positions = Position.objects.order_by('-date')
    projects = Project.objects.order_by('-date')
    educations = Education.objects.all()
    skills = Skill.objects.all()

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            your_email = form.cleaned_data["your_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")

    context = {
      'positions': positions,
      'projects':projects,
      'educations': educations,
      'skills': skills,
      'form': form
    }
    return render(request, 'home.html', context)
