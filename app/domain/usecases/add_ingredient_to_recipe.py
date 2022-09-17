from typing import List
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository


async def add_ingredient_to_recipe_use_case(recipe_id: str, ingredient_ids: List[str]) -> bool:
    repo = SqlAlchemyRecipeRepository()
    await repo.add_ingredient_to_recipe(recipe_id, ingredient_ids)
