import typing
from graphql_types.dtos.recipe import IngredientDto
from graphql_types.recipe import Recipe
from database import models
from sqlalchemy import select


async def recipes_with_ingredients_use_case(ingredients: typing.List[IngredientDto]) -> typing.List[Recipe]:
    async with models.get_session() as s:
        sql = select(models.Recipe).order_by(models.Recipe.name)
        db_recipes = (await s.execute(sql)).scalars().unique().all()
    return db_recipes
