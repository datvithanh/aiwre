from django.shortcuts import render
from .models import ProfessionalExperience, Mission

def index(request):
    return render(request, 'index.html')

def missions(request):
    missions = Mission.objects.all()
    return render(request, 'missions.html', {'missions': missions})

def members(request):
    pass

def activities(request):
    pass

def projects(request):
    pass

def researchCooperation(request):
    pass

def contacts(request):
    pass