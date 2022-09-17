from typing import List
import strawberry
from app.application.graphql_types.dtos import CreateIngredient, CreateRecipe
from app.domain.usecases.create_ingredient import create_ingredient_use_case
from app.domain.usecases.create_recipe import create_recipe_use_case
from app.domain.usecases.add_ingredient_to_recipe import add_ingredient_to_recipe_use_case


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


    @strawberry.field
    async def add_ingredient_to_recipe(self, recipe_id: str, ingredient_ids: List[str]) -> bool:
        print('Request to addIngredientToRecipe')
        await add_ingredient_to_recipe_use_case(recipe_id, ingredient_ids)
        return True
