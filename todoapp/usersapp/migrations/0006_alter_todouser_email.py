# Generated by Django 3.2.9 on 2022-09-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0005_remove_todouser_e_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todouser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
