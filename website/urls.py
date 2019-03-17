from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('missions', views.missions, name='missions'),
    path('members', views.members, name='members'),
    path('activities', views.activities, name='activities'),
    path('projects', views.projects, name='projects'),
    path('research-cooperation', views.researchCooperation, name='research-cooperation'),
    path('contacts', views.contacts, name='contacts'),

]
