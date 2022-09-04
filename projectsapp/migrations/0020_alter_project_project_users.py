# Generated by Django 3.2.9 on 2022-09-04 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectsapp', '0019_alter_project_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
