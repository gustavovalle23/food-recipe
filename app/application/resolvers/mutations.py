import strawberry
from kink import di
from typing import List

from app.application.graphql_types.dtos import CreateIngredient, CreateRecipe
from app.domain.usecases.create_ingredient import CreateIngredientUseCase
from app.domain.usecases.create_recipe import CreateRecipeUseCase
from app.domain.usecases.add_ingredient_to_recipe import AddIngredientToRecipeUseCase


@strawberry.type
class Mutation:

    @strawberry.field
    async def create_ingredient(self, ingredient: CreateIngredient) -> bool:
        print('Request to createIngredient')
        use_case: CreateIngredientUseCase = di[CreateIngredientUseCase]
        return await use_case.perform(ingredient)

    @strawberry.field
    async def create_recipe(self, recipe: CreateRecipe) -> bool:
        print('Request to createRecipe')
        use_case: CreateRecipeUseCase = di[CreateRecipeUseCase]
        return await use_case.perform(recipe)

    @strawberry.field
    async def add_ingredient_to_recipe(self, recipe_id: str, ingredient_ids: List[str]) -> bool:
        print('Request to addIngredientToRecipe')
        use_case: AddIngredientToRecipeUseCase = di[AddIngredientToRecipeUseCase]
        return await use_case.perform(recipe_id, ingredient_ids)
