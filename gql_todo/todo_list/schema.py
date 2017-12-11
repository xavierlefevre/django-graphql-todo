from graphene import relay, AbstractType
from graphene_django import DjangoConnectionField, DjangoObjectType

from gql_todo.todo_list.models import Item


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node, )


class Query(AbstractType):
    items = DjangoConnectionField(
        ItemNode, description='An item of the Todo list')
