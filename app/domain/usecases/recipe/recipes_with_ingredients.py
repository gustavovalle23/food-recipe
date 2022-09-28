import typing
from kink import inject

from app.infra.models import Recipe
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository


@inject
class FindRecipesWithIngredientsUseCase:
    def __init__(self, recipe_repository: SqlAlchemyRecipeRepository) -> None:
        self._recipe_repo = recipe_repository

    async def perform(self, ingredient_ids: typing.List[int]) -> typing.List[Recipe]:
        return await self._recipe_repo.find_recipes_with_ingredients(ingredient_ids)
