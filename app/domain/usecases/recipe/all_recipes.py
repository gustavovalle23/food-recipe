from typing import List
from kink import inject

from app.infra.models import Recipe
from app.domain.contracts.repos.recipe import RecipeRepository


@inject
class FindAllRecipesUseCase:
    def __init__(self, recipe_repository: RecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self) -> List[Recipe]:
        return await self._recipe_repo.find_all_recipes()
