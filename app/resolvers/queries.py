import strawberry
from typing import List
from app.shared.builders import IngredientBuilder

from app.usecases.all_recipes import find_all_recipes
from app.usecases.all_ingredients import find_all_ingredients_use_case
from app.usecases.recipes_with_ingredients import recipes_with_ingredients_use_case
from app.graphql_types.recipe import Ingredient, Recipe, UnitMeasurement


@strawberry.type
class Query:

    @strawberry.field
    def available_recipes(self) -> List[Recipe]:
        print('Request to availableRecipes')
        return find_all_recipes()

    @strawberry.field
    async def available_ingredients(self) -> List[Ingredient]:
        print('Request to availableIngredients')
        ingredients_db = await find_all_ingredients_use_case()
        ingredients = IngredientBuilder.buid_list(ingredients_db)
        return ingredients

    @strawberry.field
    def recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        print(f'Request to recipesWithIngredients: {ingredient_ids}')
        return recipes_with_ingredients_use_case(ingredient_ids)
