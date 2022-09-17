import inspect
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.domain.contracts.repos import RecipeRepository
from app.infra.errors.common import OnlyImplementationsAbstractMethodsAllowedException
from app.infra.models import get_session, IngredientRecipe, Recipe


class SqlAlchemyRecipeRepository(RecipeRepository):
    def __init__(self) -> None:
        methods_in_class = inspect.getmembers(
            SqlAlchemyRecipeRepository, predicate=inspect.isfunction)
        methods_in_super_class = inspect.getmembers(
            RecipeRepository, predicate=inspect.isfunction)
        if len(methods_in_class) != len(methods_in_super_class)+1:
            raise OnlyImplementationsAbstractMethodsAllowedException
        super().__init__()

    async def find_recipes_with_ingredients(self, ingredient_ids: List[int]) -> List[Recipe]:
        async with get_session() as session:
            sql = select(IngredientRecipe).where(
                IngredientRecipe.c.ingredient_id.in_([])
            )
            recipes = (await session.execute(sql)).scalars().unique().all()
        return recipes

    async def find_all_recipes(self) -> List[Recipe]:

        async with get_session() as session:
            # sql = select(Recipe).select_from(Ingredient).join(Ingredient.recipes)
            sql = select(Recipe).options(joinedload(Recipe.ingredients))
            recipes = (await session.execute(sql)).scalars().unique().all()
        return recipes
