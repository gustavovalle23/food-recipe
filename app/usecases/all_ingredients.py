from typing import List

from app.infra.models import Ingredient
from app.infra.repositories.ingredient import SqlAlchemyIngredientRepository


async def find_all_ingredients_use_case() -> List[Ingredient]:
    ingredient_repository = SqlAlchemyIngredientRepository()
    return await ingredient_repository.find_all_ingredients()
