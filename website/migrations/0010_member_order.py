# Generated by Django 2.1.7 on 2019-04-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20190401_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
