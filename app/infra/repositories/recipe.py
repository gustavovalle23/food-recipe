from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.domain.contracts.repos import RecipeRepository
from app.infra.models import get_session, IngredientRecipe, Recipe


class SqlAlchemyRecipeRepository(RecipeRepository):
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
