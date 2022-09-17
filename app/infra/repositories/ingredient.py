from typing import List
from sqlalchemy import select, insert

from app.domain.contracts.repos import IngredientRepository
from app.application.graphql_types.recipe import Ingredient as IngredientDto
from app.infra.models import Ingredient, get_session


class SqlAlchemyIngredientRepository(IngredientRepository):
    async def find_all_ingredients(self) -> List[Ingredient]:
        async with get_session() as session:
            sql = select(Ingredient).order_by(Ingredient.name)
            ingredients = (await session.execute(sql)).scalars().unique().all()
        return ingredients

    async def save(self, ingredient: IngredientDto) -> Ingredient:
        async with get_session() as session:
            sql = insert(Ingredient).values(
                name=ingredient.name,
                quantity=ingredient.quantity,
                unit_measurement=ingredient.unit_measurement.name,
            )

            await session.execute(sql)
            await session.commit()

    async def find_ingredients_by_name(self, name: str) -> Ingredient | None:
        async with get_session() as session:
            sql = select(Ingredient).filter(Ingredient.name == name)
            ingredients = (await session.execute(sql)).scalars().unique().all()
        return ingredients
