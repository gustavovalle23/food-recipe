import strawberry
from typing import List

from app.infra.shared.builders import IngredientBuilder, RecipeBuilder
from app.domain.usecases.all_recipes import find_all_recipes
from app.domain.usecases.all_ingredients import find_all_ingredients_use_case
from app.domain.usecases.recipes_with_ingredients import recipes_with_ingredients_use_case
from app.application.graphql_types.recipe import Ingredient, Recipe


@strawberry.type
class Query:

    @strawberry.field
    async def available_recipes(self) -> List[Recipe]:
        print('Request to availableRecipes')
        recipes_db = await find_all_recipes()
        return RecipeBuilder.build_list(recipes_db)

    @strawberry.field
    async def available_ingredients(self) -> List[Ingredient]:
        print('Request to availableIngredients')
        ingredients_db = await find_all_ingredients_use_case()
        return IngredientBuilder.build_list(ingredients_db)

    @strawberry.field
    async def recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        print(f'Request to recipesWithIngredients: {ingredient_ids}')
        recipes_db = await recipes_with_ingredients_use_case(ingredient_ids)
        return RecipeBuilder.build_list(recipes_db)
