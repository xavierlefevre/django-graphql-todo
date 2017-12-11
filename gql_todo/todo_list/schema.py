import graphene
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoConnectionField, DjangoObjectType

from gql_todo.todo_list.models import Item


class CreateItem(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        list_id = graphene.Int()

    item = graphene.Field(lambda: ItemNode)

    def mutate(self, info, text, list_id):
        item = Item(list_id=list_id, text=text).save()
        return CreateItem(item=item)


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node, )


class Query(AbstractType):
    items = DjangoConnectionField(
        ItemNode, description='An item of the Todo list')


class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
