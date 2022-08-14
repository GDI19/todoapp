from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer