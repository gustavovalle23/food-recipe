import strawberry
import typing

from mocks.recipes import get_all_recipes
from schemas.dtos.recipe import IngredientDto
from schemas.recipe import Recipe, UnitMeasurement
from usecases.recipes_with_ingredients import recipes_with_ingredients_use_case


@strawberry.type
class Query:
    available_recipes: typing.List[Recipe] = strawberry.field(
        resolver=get_all_recipes
    )

    @strawberry.field
    def recipes_with_ingredients(self, ingredients: typing.List[IngredientDto]) -> Recipe:
        return recipes_with_ingredients_use_case(ingredients)
