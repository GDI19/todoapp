from django.contrib import admin
from .models import Project, ToDo


# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_link',)
    list_filter = ('project_name',)

# admin.site.register(To Do)
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('todo_author', 'todo_text',  'todo_project', 'todo_creation_date', 'todo_updated_date', 'todo_is_active')
    list_filter = ('todo_project', 'todo_creation_date', 'todo_updated_date')
    fields = ['todo_author', 'todo_text', 'todo_project', ('todo_creation_date', 'todo_updated_date'), 'todo_is_active']