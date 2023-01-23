from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer

from usersapp.serializers import UserModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    project_users = StringRelatedField(many=True) # users будут представлены методом __str__ в моделях

    class Meta:
        model = Project
        fields = '__all__'

class ProjectModelSerializerBase(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    # todo_author = UserModelSerializer() # на выходе появится вложенный словарь
    # todo_project = ProjectModelSerializer()
    todo_author = StringRelatedField()
    todo_project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'


class TodoModelSerializerBase(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'