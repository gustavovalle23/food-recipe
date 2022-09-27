from sqlalchemy import insert
from kink import inject

from app.application.graphql_types.recipe import Ingredient
from app.infra.repositories.ingredient import SqlAlchemyIngredientRepository


@inject
class CreateIngredientUseCase:
    def __init__(self, ingredient_repository: SqlAlchemyIngredientRepository) -> None:
        self._ingredient_repo = ingredient_repository

    async def perform(self, ingredient: Ingredient):
        ingredients = await self._ingredient_repo.find_ingredients_by_name(ingredient.name)
        if not ingredients:
            await self._ingredient_repo.save(ingredient)
            return True
        return False
