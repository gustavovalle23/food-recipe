import strawberry
import typing
from graphql_types.dtos.recipe import IngredientDto

from mocks.recipes import get_all_recipes
from graphql_types.recipe import Recipe
from usecases.recipes_with_ingredients import recipes_with_ingredients_use_case


@strawberry.type
class Query:
    available_recipes: typing.List[Recipe] = strawberry.field(
        resolver=get_all_recipes
    )

    @strawberry.field
    def recipes_with_ingredients(self, ingredients: typing.List[IngredientDto]) -> Recipe:
        return recipes_with_ingredients_use_case(ingredients)
