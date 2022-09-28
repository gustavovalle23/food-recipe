import abc
from typing import List
from app.infra.models import Recipe
from app.infra.shared.utils import subclass_hook_return


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

    @abc.abstractmethod
    async def add_ingredient_to_recipe(self, recipe_id: str, ingredient_ids: List[str]) -> bool:
        raise NotImplementedError
