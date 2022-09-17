import strawberry
from app.application.graphql_types.dtos import CreateIngredient
from app.domain.usecases.create_ingredient import create_ingredient_use_case


@strawberry.type
class Mutation:

    @strawberry.field
    async def create_ingredient(self, ingredient: CreateIngredient) -> bool:
        print('Request to createIngredient')
        return await create_ingredient_use_case(ingredient)
