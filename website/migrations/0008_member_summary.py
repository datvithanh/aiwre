# Generated by Django 2.1.6 on 2019-04-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20190401_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='summary',
            field=models.CharField(default='', max_length=1023),
        ),
    ]