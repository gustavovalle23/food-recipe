import strawberry
import typing
from mocks.recipes import get_all_recipes

from schemas.recipe import Recipe


@strawberry.type
class Query:
    available_recipes: typing.List[Recipe] = strawberry.field(
        resolver=get_all_recipes
    )
