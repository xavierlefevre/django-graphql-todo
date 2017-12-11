from graphene import ObjectType, Schema

import gql_todo.todo_list.schema


class Query(gql_todo.todo_list.schema.Query, ObjectType):
    pass


class Mutation(gql_todo.todo_list.schema.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
