from graphene import relay, AbstractType
from graphene_django import DjangoConnectionField, DjangoObjectType

from gql_todo.todo_list.models import Item, List


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node, )


class ListNode(DjangoObjectType):
    class Meta:
        model = List
        interfaces = (relay.Node, )


class Query(AbstractType):
    item = relay.Node.Field(ItemNode)
    items = DjangoConnectionField(
        ItemNode, description='An item of the Todo list')
    list = relay.Node.Field(ListNode)
    lists = DjangoConnectionField(
        ListNode, description='A list')
