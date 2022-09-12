from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from projectsapp.views import ProjectModelViewSet, ToDoModelViewSet
from usersapp.views import UserCustomViewSet


schema_view = get_schema_view(
    openapi.Info(
        title = 'Todo app',
        default_version= '1.0',
        description= 'Documentation to Todo application',
        contact= openapi.Contact(email='admin@admin.ru'),
        license= openapi.License(name='MIT License'),
    ),
    public = True,
    permission_classes= [permissions.AllowAny],
)


router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/<str:version>/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

    path('swagger<str:format>/', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),

    # path('filter/kwargs/<str:name>/', ProjectKwargsFilterView.as_view()),
]
