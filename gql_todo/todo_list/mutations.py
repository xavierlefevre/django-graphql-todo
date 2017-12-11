import graphene

from gql_todo.todo_list.models import Item
from gql_todo.todo_list.schema import ItemNode


class CreateItem(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        list_id = graphene.Int()

    item = graphene.Field(lambda: ItemNode)

    def mutate(self, info, text, list_id):
        item = Item(list_id=list_id, text=text).save()
        return CreateItem(item=item)


class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
