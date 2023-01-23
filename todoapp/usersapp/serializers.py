from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField, ModelSerializer
from .models import TodoUser


class UserModelSerializer(ModelSerializer):
    #url = HyperlinkedIdentityField(view_name ="usersapp:users-detail")
    class Meta:
        model = TodoUser
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email']


class UserModelSerializerWithStaff(ModelSerializer):
    #url = HyperlinkedIdentityField(view_name="usersapp:users-detail")
    class Meta:
        model = TodoUser
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']