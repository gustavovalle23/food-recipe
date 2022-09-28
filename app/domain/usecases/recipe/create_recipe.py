from kink import inject

from app.application.graphql_types.dtos import CreateRecipe
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository


@inject
class CreateRecipeUseCase:
    def __init__(self, recipe_repository: SqlAlchemyRecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self, recipe: CreateRecipe):
        await self._recipe_repo.save(recipe)
        return True
