from django.shortcuts import render
from .models import Janico, Experience, Projects


def index(request):
    janico = Janico.objects.all()
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    
    for i in projects:
        stackdata = i.stack.split()
        
    context = {
        'janico':janico,
        'experience':experience,
        'projects':projects,
        'stackdata':stackdata
    }
    return render(request, "App/index.html", context)