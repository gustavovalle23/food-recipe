import inspect
from kink import inject
from typing import List
from sqlalchemy import select, insert

from app.application.graphql_types.recipe import Ingredient as IngredientDto
from app.domain.contracts.repos.ingredient import IngredientRepository
from app.infra.errors.common import OnlyImplementationsAbstractMethodsAllowedException
from app.infra.models import Ingredient, get_session


@inject
class SqlAlchemyIngredientRepository(IngredientRepository):
    def __init__(self) -> None:
        methods_in_class = inspect.getmembers(
            SqlAlchemyIngredientRepository, predicate=inspect.isfunction)
        methods_in_super_class = inspect.getmembers(
            IngredientRepository, predicate=inspect.isfunction)
        if len(methods_in_class) != len(methods_in_super_class)+1:
            raise OnlyImplementationsAbstractMethodsAllowedException
        super().__init__()

    async def find_all_ingredients(self) -> List[Ingredient]:
        async with get_session() as session:
            sql = select(Ingredient).order_by(Ingredient.id)
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
