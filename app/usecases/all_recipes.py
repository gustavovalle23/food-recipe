from typing import List

from app.infra.models import Recipe
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository

async def find_all_recipes() -> List[Recipe]:
    recipe_repo = SqlAlchemyRecipeRepository()
    return await recipe_repo.find_all_recipes()
