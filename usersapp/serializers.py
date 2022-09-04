from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import TodoUser


class UserModelSerializer(HyperlinkedModelSerializer):
    # url = HyperlinkedIdentityField(view_name ="users-detail")
    class Meta:
        model = TodoUser
        fields = ['url', 'username', 'first_name', 'last_name', 'email']


