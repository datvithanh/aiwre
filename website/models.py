import datetime
from django.db import models

#
class Member(models.Model):
    name = models.CharField(max_length=511)
    address = models.CharField(max_length=511)
    email = models.CharField(max_length=511)
    phone = models.CharField(max_length=511)
    avatar = models.CharField(max_length=511, null=True)
    research_interest = models.CharField(max_length=511)

class Education(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    college = models.CharField(max_length=511)
    degree = models.CharField(max_length=511, default='')
    location = models.CharField(max_length=511, default='')
    graduation_date = models.DateField(default=datetime.date.today)

class ProfessionalExperience(models.Model):
    timespan = models.CharField(max_length=511, default='')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=511)
    job_title = models.CharField(max_length=511, default='')

class Publication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=511)
    name = models.CharField(max_length=511, default='')

#
class ResearchActivity(models.Model):
    name = models.CharField(max_length=511)
    description = models.CharField(max_length=511, null=True)

#
class Project(models.Model):
    name = models.CharField(max_length=511)
    description = models.CharField(max_length=511, null=True)

#
class ResearchCooperation(models.Model):
    content = models.CharField(max_length=511)

#
class Mission(models.Model):
    content = models.CharField(max_length=511)