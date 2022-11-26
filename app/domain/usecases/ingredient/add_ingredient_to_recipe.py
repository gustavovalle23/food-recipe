from typing import List
from kink import inject

from app.domain.contracts.repos.recipe import RecipeRepository


@inject
class AddIngredientToRecipeUseCase:
    def __init__(self, recipe_repository: RecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self, recipe_id: str, ingredient_ids: List[str]) -> bool:
        await self._recipe_repo.add_ingredient_to_recipe(recipe_id, ingredient_ids)
        return True
