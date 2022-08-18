from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import UserModelSerializer
from rest_framework import mixins, viewsets


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = UserModelSerializer

