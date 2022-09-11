from typing import List
from app.infra.models import Ingredient
from app.infra.repositories.ingredient import find_all_ingredients_repository

async def find_all_ingredients_use_case() -> List[Ingredient]:
    ingredients = await find_all_ingredients_repository()
    return ingredients
