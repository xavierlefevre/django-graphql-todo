from graphene import ObjectType, Schema

import gql_todo.todo_list.schema


class Query(gql_todo.todo_list.schema.Query, ObjectType):
    pass


schema = Schema(query=Query)
