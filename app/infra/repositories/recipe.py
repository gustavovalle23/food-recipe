from typing import List
from sqlalchemy import select

from app.infra.models import get_session, IngredientRecipe, Recipe

async def find_recipes_with_ingredients_repository(ingredient_ids: List[int]):
    async with get_session() as session:
        # sql = select(Recipe).order_by(Recipe.name)
        sql = select(IngredientRecipe).where(IngredientRecipe.c.ingredient_id.in_([]))

        recipes = (await session.execute(sql)).scalars().unique().all()
    return recipes


async def find_all_recipes() -> List[Recipe]:
    async with get_session() as session:
        sql = select(Recipe).order_by(Recipe.name)
        recipes = (await session.execute(sql)).scalars().unique().all()
    return recipes
