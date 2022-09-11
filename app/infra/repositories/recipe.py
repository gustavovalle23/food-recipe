from typing import List
from sqlalchemy import select

from app.infra.models import get_session, Recipe

async def find_recipes_with_ingredients_repository(ingredient_ids: List[int]):
    async with get_session() as session:
        sql = select(Recipe).order_by(Recipe.name)
        recipes = (await session.execute(sql)).scalars().unique().all()
    return recipes

