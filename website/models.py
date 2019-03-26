from django.db import models

#
class Member(models.Model):
    name = models.CharField(max_length=1023)
    address = models.CharField(max_length=1023)
    email = models.CharField(max_length=1023)
    phone = models.CharField(max_length=1023)
    avatar = models.CharField(max_length=1023, null=True)
    research_interest = models.CharField(max_length=1023)

class Education(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=1023)

class ProfessionalExperience(models.Model):
    timespan = models.CharField(max_length=1023, default='')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=1023)

class Publication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=1023)

#
class ResearchActivity(models.Model):
    name = models.CharField(max_length=1023)
    description = models.CharField(max_length=1023, null=True)

#
class Project(models.Model):
    name = models.CharField(max_length=1023)
    description = models.CharField(max_length=1023, null=True)

#
class ResearchCooperation(models.Model):
    content = models.CharField(max_length=1023)

#
class Mission(models.Model):
    content = models.CharField(max_length=1023)