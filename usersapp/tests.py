from django.test import TestCase
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate,APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
from .views import UserCustomViewSet
from .models import TodoUser


class TestUserViewSet(TestCase):

    def setUp(self):
        pass

    def test_get_users_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_by_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'first_name': 'dim', 'last_name': 'gi', 'email': 'dig@ya.ru'}, format='json')
        view = UserCustomViewSet.as_view({'post':'update'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_update_by_admin(self):
    #     factory = APIRequestFactory()
    #     user = TodoUser.objects.create_user(pk='1', username='Notadmin', email='notadmin@y.ru', password='notadminDRF5675')
    #     request = factory.post(f'api/users/1/', {'first_name': 'dim', 'last_name': 'gi', 'email': 'dig@ya.ru'}, format='json')
    #     admin = TodoUser.objects.create_superuser('admin', 'admin@y.ru', 'adminDRF5675')
    #     force_authenticate(request, admin)
    #     view = UserCustomViewSet.as_view({'post':'update'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


    def tearDown(self):
        pass
