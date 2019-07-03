from django.contrib import admin
from .models import *

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1

class ProfessionalExperience(admin.StackedInline):
    model = ProfessionalExperience
    extra = 1

class PublicationInline(admin.StackedInline):
    model = Publication
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    list_display_links = ['name']
    inlines = [EducationInline, ProfessionalExperience, PublicationInline]

class Project(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProjectObjective]

admin.site.register(Member, MemberAdmin)
admin.site.register(Project)
admin.site.register(ResearchCooperation)
admin.site.register(ResearchActivity)
admin.site.register(Mission)