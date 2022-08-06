from django.db import models

class TodoUser(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    e_mail = models.EmailField(unique=True)