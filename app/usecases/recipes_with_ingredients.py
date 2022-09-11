import typing

from app.graphql_types.recipe import Recipe
from app.infra.repositories.recipe import find_recipes_with_ingredients_repository


async def recipes_with_ingredients_use_case(ingredient_ids: typing.List[int]) -> typing.List[Recipe]:
    recipes = await find_recipes_with_ingredients_repository(ingredient_ids)
    return recipes
