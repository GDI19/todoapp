from rest_framework import mixins, viewsets, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, ToDoFilter
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, TodoModelSerializer, ProjectModelSerializerBase, TodoModelSerializerBase
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.generics import ListAPIView


# class ProjectPageNumberPagination(PageNumberPagination):
#     page_size = 1
#
#     def get_paginated_response(self, data):
#         return Response(data)
#
# class ToDoPageNumberPagination(PageNumberPagination):
#     page_size = 1
#
#     def get_paginated_response(self, data):
#         return Response(data)

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
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectModelSerializer
        return ProjectModelSerializerBase


class ToDoModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    # pagination_class = ToDoPageNumberPagination
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ToDoFilter

    def perform_destroy(self, instance):
          instance.todo_is_active = False
          instance.save()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TodoModelSerializer
        return TodoModelSerializerBase
