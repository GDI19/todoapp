# Generated by Django 3.2.9 on 2022-09-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_remove_todouser_user_name'),
        ('projectsapp', '0013_alter_project_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_users',
            field=models.ManyToManyField(to='usersapp.TodoUser'),
        ),
    ]
