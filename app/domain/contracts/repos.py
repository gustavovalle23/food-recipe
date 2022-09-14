import abc
from typing import List
from app.infra.models import Ingredient, Recipe

class IngredientRepository(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    async def find_all_ingredients(self) -> List[Ingredient]:
        raise NotImplementedError


class RecipeRepository(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    async def find_recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        raise NotImplementedError

    @abc.abstractmethod
    async def find_all_recipes(self) -> List[Recipe]:
        raise NotImplementedError
