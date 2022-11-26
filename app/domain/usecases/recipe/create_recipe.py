from kink import inject

from app.application.graphql_types.dtos import CreateRecipe
from app.domain.contracts.repos.recipe import RecipeRepository


@inject
class CreateRecipeUseCase:
    def __init__(self, recipe_repository: RecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self, recipe: CreateRecipe):
        await self._recipe_repo.save(recipe)
        return True
