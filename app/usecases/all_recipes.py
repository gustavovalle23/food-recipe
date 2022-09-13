from typing import List

from app.infra.models import Recipe
from app.infra.repositories.recipe import find_all_recipes

async def find_all_recipes() -> List[Recipe]:
    recipes = await find_all_recipes()
    return recipes
