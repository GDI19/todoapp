from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import UserModelSerializer, UserModelSerializerWithStaff
from rest_framework import mixins, viewsets


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1.1':
            return UserModelSerializerWithStaff
        return UserModelSerializer
