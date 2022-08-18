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


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter

    def destroy(self, request, pk=None):
        self.item_to_delete = ToDo.objects.get(pk=pk)
        self.item_to_delete.todo_is_active = False
