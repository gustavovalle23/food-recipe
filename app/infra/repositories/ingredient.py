from typing import List
from sqlalchemy import select
from app.domain.contracts.repos import IngredientRepository

from app.infra.models import Ingredient, get_session


class SqlAlchemyIngredientRepository(IngredientRepository):
    async def find_all_ingredients(self) -> List[Ingredient]:
        async with get_session() as session:
            sql = select(Ingredient).order_by(Ingredient.name)
            ingredients = (await session.execute(sql)).scalars().unique().all()
        return ingredients
