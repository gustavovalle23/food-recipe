import abc
from typing import List
from app.infra.models import Ingredient, Recipe
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

    @abc.abstractmethod
    async def save(self, recipe) -> Recipe:
        raise NotImplementedError
