# Generated by Django 2.1.7 on 2019-04-01 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190326_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='content',
        ),
        migrations.RemoveField(
            model_name='professionalexperience',
            name='content',
        ),
        migrations.AddField(
            model_name='education',
            name='college',
            field=models.CharField(default='', max_length=511),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(default='', max_length=511),
        ),
        migrations.AddField(
            model_name='education',
            name='graduation_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.CharField(default='', max_length=511),
        ),
        migrations.AddField(
            model_name='professionalexperience',
            name='company_name',
            field=models.CharField(default='', max_length=511),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professionalexperience',
            name='job_title',
            field=models.CharField(default='', max_length=511),
        ),
        migrations.AddField(
            model_name='professionalexperience',
            name='timespan',
            field=models.CharField(default='', max_length=511),
        ),
        migrations.AddField(
            model_name='publication',
            name='name',
            field=models.CharField(default='', max_length=511),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.CharField(max_length=511, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='member',
            name='research_interest',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='mission',
            name='content',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=511, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='researchactivity',
            name='description',
            field=models.CharField(max_length=511, null=True),
        ),
        migrations.AlterField(
            model_name='researchactivity',
            name='name',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='researchcooperation',
            name='content',
            field=models.CharField(max_length=511),
        ),
    ]