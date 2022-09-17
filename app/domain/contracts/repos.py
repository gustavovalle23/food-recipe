import abc
from typing import List
from app.infra.models import Ingredient, Recipe
from app.shared.utils import subclass_hook_return


class IngredientRepository(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return subclass_hook_return(subclass)

    @abc.abstractmethod
    async def find_all_ingredients(self) -> List[Ingredient]:
        raise NotImplementedError


class RecipeRepository(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return subclass_hook_return(subclass)

    @abc.abstractmethod
    async def find_recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        raise NotImplementedError

    @abc.abstractmethod
    async def find_all_recipes(self) -> List[Recipe]:
        raise NotImplementedError
