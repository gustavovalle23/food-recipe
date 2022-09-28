from typing import List
from kink import inject, di

from app.infra.models import Recipe
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository


@inject
class FindAllRecipesUseCase:
    def __init__(self, recipe_repository: SqlAlchemyRecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self) -> List[Recipe]:
        return await self._recipe_repo.find_all_recipes()
