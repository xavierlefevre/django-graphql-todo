from graphene import ObjectType, Schema

import gql_todo.todo_list.schema
import gql_todo.todo_list.mutations


class Query(gql_todo.todo_list.schema.Query, ObjectType):
    pass


class Mutation(gql_todo.todo_list.mutations.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
