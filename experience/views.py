from django.shortcuts import render
from experience.models import Position

def experience_item(request):
    positions = Position.objects.all()
    context = {
        'positions': positions
    }
    return render(request, 'experience.html', context)
