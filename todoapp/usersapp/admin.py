from django.contrib import admin
from .models import TodoUser

#admin.site.register(TodoUser)
@admin.register(TodoUser)
class TodoUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')