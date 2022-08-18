from django.db import models
from usersapp.models import TodoUser


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    project_link = models.URLField(max_length=200, blank=True)
    project_users = models.ManyToManyField(TodoUser)

    def __str__(self):
        return f'This is {self.project_name} project'


class ToDo(models.Model):
    todo_author = models.ForeignKey(TodoUser, on_delete=models.CASCADE)
    todo_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    todo_text = models.TextField()
    todo_creation_date = models.DateTimeField()
    todo_updated_date = models.DateTimeField()
    todo_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"This is the todo to the {self.todo_project} project"