import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.application.resolvers.queries import Query
from app.application.resolvers.mutations import Mutation


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
