from typing import List
from kink import inject

from app.infra.models import Ingredient
from app.domain.contracts.repos.ingredient import IngredientRepository


@inject
class FindAllIngredientsUseCase:
    def __init__(self, ingredient_repository: IngredientRepository) -> None:
        self._ingredient_repo = ingredient_repository

    async def perform(self) -> List[Ingredient]:
        return await self._ingredient_repo.find_all_ingredients()
