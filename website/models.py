from django.db import models

#
class Member(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True)
    research_interest = models.CharField(max_length=255)

class Education(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

class ProfessionalExperience(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

class Publication(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

#
class ResearchActivity(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

#
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

#
class ResearchCooperation(models.Model):
    content = models.CharField(max_length=255)

#
class Mission(models.Model):
    content = models.CharField(max_length=255)