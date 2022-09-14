import typing

from app.graphql_types.recipe import Recipe
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository


async def recipes_with_ingredients_use_case(ingredient_ids: typing.List[int]) -> typing.List[Recipe]:
    recipe_repo = SqlAlchemyRecipeRepository()
    return await recipe_repo.find_recipes_with_ingredients(ingredient_ids)
