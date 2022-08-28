from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer

from usersapp.serializers import UserModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    project_users = StringRelatedField(many=True) # users будут представлены методом __str__ в моделях

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    # todo_author = UserModelSerializer() # на выходе появится вложенный словарь - проблемы т.к. не массив (Array)
    # todo_project = ProjectModelSerializer()
    todo_author = StringRelatedField()  # будут представлены методом __str__ в моделях
    todo_project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
