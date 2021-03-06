# Generated by Django 2.1.7 on 2019-04-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_member_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='content',
            new_name='article',
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.CharField(default='', max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='journal',
            field=models.CharField(default='', max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='link',
            field=models.CharField(default='', max_length=511, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(default='', max_length=511, null=True),
        ),
    ]
