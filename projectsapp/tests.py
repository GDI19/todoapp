import datetime

from django.test import TestCase
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from .views import ToDoModelViewSet, ProjectModelViewSet
from usersapp.models import TodoUser
from .models import TodoUser, Project, ToDo
from django.test import TestCase


class TestCaseProjectTodoSet(TestCase):

    def setUp(self):
        self.project = mixer.blend(Project)
        self.todo1 = mixer.blend(ToDo)
        self.user = TodoUser.objects.create_user('user1', 'user1@y.ru', 'assa454545')
        TodoUser.objects.create_superuser('admin', 'admin@y.ru', 'adminDRF5675')

    def test_get_detail_by_guest(self):
        client = APIClient()
        response = client.get(f'/api/projects/{self.project.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_by_guest(self):
        client = APIClient()
        response = client.put(f'/api/projects/{self.project.pk}/', {'project_name': 'new_test_name'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_detail_by_user(self):
        client = APIClient()
        client.login(username='admin', password='adminDRF5675')
        response = client.get(f'/api/projects/{self.project.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

    def test_edit_admin(self):
        client = APIClient()
        client.login(username='admin', password='adminDRF5675')
        response = client.put(f'/api/projects/{self.project.pk}/', {'project_name': 'new_test_name', 'project_link': 'http://erg.com', 'project_users': [self.user.pk,] }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestApiTestCaseProjectTodoSet(APITestCase):

    def setUp(self):
        self.project = mixer.blend(Project)
        self.todo1 = mixer.blend(ToDo)
        self.user = TodoUser.objects.create_user('user1', 'user1@y.ru', 'assa454545')
        self.creation_date = str(datetime.datetime.today())
        self.updated_date = str(datetime.datetime.today())
        TodoUser.objects.create_superuser('admin', 'admin@y.ru', 'adminDRF5675')
        self.client.login(username='user1', password='assa454545')

    def test_get_list(self):
        response = self.client.get(f'/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        response = self.client.get(f'/api/projects/{self.project.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        self.client.logout()
        response = self.client.get(f'/api/projects/{self.project.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username='admin', password='adminDRF5675')
        response = self.client.put(f'/api/todo/{self.todo1.pk}/', {'todo_author': self.user.pk, 'todo_project': self.project.pk,
                                                                   'todo_text': 'asdfg', 'todo_creation_date': self.creation_date,
                                                                   'todo_updated_date': self.updated_date, 'todo_is_active': True
                                                                   }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_todo = json.loads(response.content)
        self.assertEqual(response_todo['todo_text'], 'asdfg')