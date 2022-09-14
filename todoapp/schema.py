import graphene
from graphene_django import DjangoObjectType
from usersapp.models import TodoUser
from projectsapp.models import ToDo, Project

class TodoUserType(DjangoObjectType):
    class Meta:
        model = TodoUser
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'
        #exclude = ['password',]



class Query(graphene.ObjectType):
    all_users = graphene.List(TodoUserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(TodoType)

    def resolve_all_users(root, info):
        return TodoUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()


schema = graphene.Schema(query=Query)