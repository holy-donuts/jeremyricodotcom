from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Project, Position, Education, Skill
from .forms import ContactForm

def home(request):
    positions = Position.objects.order_by('-date')
    projects = Project.objects.order_by('-date')
    educations = Education.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email=form.cleaned_data['from_email']
            message=form.cleaned_data['message']
            subject = f"JR.COM: NEW CONTACT FROM {from_email}"
            try:
                send_mail(subject,
                          message,
                          from_email,
                          ['jeremy.rico35@gmail.com']
                    )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            messages.success(request, 'Success! Thanks for your message!')
        else:
            messages.error(request, "Error: ReCaptcha failed :( Are you sure you're human?")
           
    else:
        form=ContactForm()
    
    context = {
        'positions': positions,
        'projects':projects,
        'educations': educations,
        'skills': skills,
        'form': form,
    }
    
    return render(request, 'home.html', context)
