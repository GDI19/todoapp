from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField

from usersapp.serializers import UserModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    project_users = StringRelatedField(many=True) # users будут представлены методом __str__ в моделях

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    todo_author = UserModelSerializer() # на выходе появится вложенный словарь
    todo_project = ProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
