from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TodoUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoUser
        fields = '__all__'


