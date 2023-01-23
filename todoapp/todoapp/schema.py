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


class TodoMutation(graphene.Mutation):
    class Arguments:
        todo_text = graphene.String(required=True)
        id = graphene.ID()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, todo_text, id):
        todo = ToDo.objects.get(pk=id)
        todo.todo_text = todo_text
        todo.save()
        return TodoMutation(todo=todo)


# ---------------------------------------------------------


class Mutation(graphene.ObjectType):
    update_todo = TodoMutation.Field()


#----------------------------------------------------------


class Query(graphene.ObjectType):
    all_users = graphene.List(TodoUserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(TodoType)

    user_by_id = graphene.Field(TodoUserType, id=graphene.Int(required=True))
    user_by_email = graphene.List(TodoUserType, email=graphene.String(required=True))

    projects_by_username = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_all_users(root, info):
        return TodoUser.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return TodoUser.objects.get(id=id)
        except TodoUser.DoesNotExist:
            return None

    def resolve_user_by_email(self, info, email=None):
        users = TodoUser.objects.all()
        if email:
            user = users.filter(email=email)
            return user

    def resolve_projects_by_username(self, info, username=None):
        projects = Project.objects.all()
        if username:
            project = projects.filter(project_users__username=username)
            return project



schema = graphene.Schema(query=Query, mutation=Mutation)