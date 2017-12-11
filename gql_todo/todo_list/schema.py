from graphene import relay, AbstractType
from graphene_django import DjangoConnectionField, DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from gql_todo.todo_list.models import Item, List


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        filter_fields = {
            'text': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class ListNode(DjangoObjectType):
    class Meta:
        model = List
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(AbstractType):
    item = relay.Node.Field(ItemNode)
    items = DjangoFilterConnectionField(
        ItemNode, description='An item of the Todo list')
    list = relay.Node.Field(ListNode)
    lists = DjangoFilterConnectionField(
        ListNode, description='A list')
