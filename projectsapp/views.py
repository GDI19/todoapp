from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, ToDoFilter
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


# class ProjectKwargsFilterView(ListAPIView):
#    serializer_class = ProjectModelSerializer
#
#    def get_queryset(self):
#        name = self.kwargs['name']
#        return Project.objects.filter(project_name__contains=name)


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    # filterset_fields = ['project_name']
    filterset_class = ProjectFilter


class ToDoModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter

    def perform_destroy(self, instance):
          instance.todo_is_active = False
          instance.save()
