from app.infra.models import get_session, Recipe, Ingredient
from sqlalchemy import insert


async def seeds():
    async with get_session() as session:
        sql = insert(Recipe).values(
            name='Pie',
            active=True,
            link='https://www.tasteofhome.com/recipes/world-s-best-lemon-pie')
        await session.execute(sql)

        sql = insert(Recipe).values(
            name='Easy pancakes',
            active=True,
            link='https://www.bbcgoodfood.com/recipes/easy-pancakes')
        await session.execute(sql)

        sql = insert(Recipe).values(
            name='Chilli con carne',
            active=True,
            link='https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe')
        await session.execute(sql)

        sql = insert(Recipe).values(
            name='Yummy golden syrup flapjacks',
            active=True,
            link='https://www.bbcgoodfood.com/recipes/yummy-golden-syrup-flapjacks')
        await session.execute(sql)

        await session.commit()
