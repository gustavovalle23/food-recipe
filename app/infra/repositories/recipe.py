from typing import List
from sqlalchemy import select

from app.infra.models import get_session, IngredientRecipe, Recipe


from typing import List
from sqlalchemy import select
from app.domain.contracts.repos import RecipeRepository

from app.infra.models import get_session


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
            sql = select(Recipe).order_by(Recipe.name)
            recipes = (await session.execute(sql)).scalars().unique().all()
        return recipes
