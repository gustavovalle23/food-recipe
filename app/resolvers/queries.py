import strawberry
from typing import List

from app.usecases.all_recipes import find_all_recipes
from app.usecases.all_ingredients import find_all_ingredients_use_case
from app.usecases.recipes_with_ingredients import recipes_with_ingredients_use_case
from app.graphql_types.recipe import Ingredient, Recipe


@strawberry.type
class Query:

    @strawberry.field
    def available_recipes(self) -> List[Recipe]:
        print(f'Request to availableRecipes')
        return find_all_recipes()

    @strawberry.field
    def available_ingredients(self) -> List[Ingredient]:
        print(f'Request to availableIngredients')
        return find_all_ingredients_use_case()

    @strawberry.field
    def recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        print(f'Request to recipesWithIngredients: {ingredient_ids}')
        return recipes_with_ingredients_use_case(ingredient_ids)
