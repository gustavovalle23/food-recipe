from sqlalchemy import select
from infra import models

async def find_all_recipes():
    async with models.get_session() as s:
        sql = select(models.Recipe).order_by(models.Recipe.id)
        response = (await s.execute(sql)).scalars().unique().all()
    return response
