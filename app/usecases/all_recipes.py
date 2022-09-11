from typing import List
from sqlalchemy import select
from app.infra.models import Recipe, get_session

async def find_all_recipes() -> List[Recipe]:
    async with get_session() as s:
        sql = select(Recipe).order_by(Recipe.id)
        response = (await s.execute(sql)).scalars().unique().all()
    return response
