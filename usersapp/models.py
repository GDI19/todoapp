from django.db import models

class TodoUser(models.Model):
    # user_name = models.CharField(max_length=64, default='Пользователь')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    e_mail = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'