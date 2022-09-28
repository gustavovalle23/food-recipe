import abc
from typing import List
from app.infra.models import Ingredient
from app.infra.shared.utils import subclass_hook_return
from app.application.graphql_types.recipe import Ingredient as IngredientDto


class IngredientRepository(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return subclass_hook_return(subclass)

    @abc.abstractmethod
    async def find_all_ingredients(self) -> List[Ingredient]:
        raise NotImplementedError

    @abc.abstractmethod
    async def save(self, ingredient: IngredientDto) -> Ingredient:
        raise NotImplementedError

    @abc.abstractmethod
    async def find_ingredients_by_name(self, name: str) -> Ingredient | None:
        raise NotImplementedError
