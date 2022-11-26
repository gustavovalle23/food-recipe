import typing
from kink import inject

from app.infra.models import Recipe
from app.domain.contracts.repos.recipe import RecipeRepository


@inject
class FindRecipesWithIngredientsUseCase:
    def __init__(self, recipe_repository: RecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self, ingredient_ids: typing.List[int]) -> typing.List[Recipe]:
        return await self._recipe_repo.find_recipes_with_ingredients(ingredient_ids)
