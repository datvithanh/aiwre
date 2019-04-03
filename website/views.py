from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def missions(request):
    missions = Mission.objects.all()
    return render(request, 'missions.html', {'missions': missions})

def members(request):
    members = Member.objects.all().order_by('order')
    return render(request, 'members.html', {'members': members})

def activities(request):
    ras = ResearchActivity.objects.all()
    return render(request, 'research_activities.html', {'ras': ras})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def researchCooperation(request):
    rcs = ResearchCooperation.objects.all()
    return render(request, 'research_coopereations.html', {'rcs': rcs})

def contacts(request):
    pass