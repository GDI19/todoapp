from django_filters import rest_framework as filters
from .models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    project_name = filters.CharFilter(lookup_expr='contains') # contains для поиска по части имени

    class Meta:
        model = Project
        fields = ['project_name']


class ToDoFilter(filters.FilterSet):
    todo_project = filters.CharFilter(field_name='todo_project', lookup_expr='contains') # contains для поиска по части имени
    todo_creation_date_gt = filters.DateFilter(field_name='todo_creation_date', lookup_expr='date__gt')
    todo_creation_date_lt = filters.DateFilter(field_name='todo_creation_date', lookup_expr='date__lt')

    class Meta:
        model = ToDo
        fields = ['todo_project', 'todo_creation_date']