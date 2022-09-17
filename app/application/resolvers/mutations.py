import strawberry
from app.application.graphql_types.dtos import CreateIngredient, CreateRecipe
from app.domain.usecases.create_ingredient import create_ingredient_use_case
from app.domain.usecases.create_recipe import create_recipe_use_case


@strawberry.type
class Mutation:

    @strawberry.field
    async def create_ingredient(self, ingredient: CreateIngredient) -> bool:
        print('Request to createIngredient')
        return await create_ingredient_use_case(ingredient)

    @strawberry.field
    async def create_recipe(self, recipe: CreateRecipe) -> bool:
        print('Request to createRecipe')
        await create_recipe_use_case(recipe)
        return True
