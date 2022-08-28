from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, ToDoFilter
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.generics import ListAPIView


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        return Response(data)

class ToDoPageNumberPagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        return Response(data)

# class ProjectKwargsFilterView(ListAPIView):
#    serializer_class = ProjectModelSerializer
#
#    def get_queryset(self):
#        name = self.kwargs['name']
#        return Project.objects.filter(project_name__contains=name)


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # pagination_class = ProjectPageNumberPagination
    # filterset_fields = ['project_name']
    filterset_class = ProjectFilter


class ToDoModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    # pagination_class = ToDoPageNumberPagination
    filterset_class = ToDoFilter

    def perform_destroy(self, instance):
          instance.todo_is_active = False
          instance.save()
