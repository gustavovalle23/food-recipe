import inspect
from typing import List
from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from app.domain.contracts.repos import RecipeRepository
from app.application.graphql_types.recipe import Recipe as RecipeDto
from app.infra.errors.common import OnlyImplementationsAbstractMethodsAllowedException
from app.infra.models import Ingredient, get_session, IngredientRecipe, Recipe


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

    async def save(self, recipe: RecipeDto) -> Recipe:
        async with get_session() as session:
            sql = insert(Recipe).values(
                name=recipe.name,
                link=recipe.link,
            )
            await session.execute(sql)
            await session.commit()

    async def add_ingredient_to_recipe(self, recipe_id: str, ingredient_ids: List[str]) -> bool:
        async with get_session() as session:
            sql = select(Recipe).options(joinedload(
                Recipe.ingredients)).where(Recipe.id == recipe_id)
            recipes: List[Recipe] = (await session.execute(sql)).scalars().unique().all()
            recipe = recipes[0]
            ingredients_already_added = [
                ingredient.id for ingredient in recipe.ingredients
            ]

            sql = select(Ingredient).where(
                Ingredient.id.in_(ingredient_ids)
            ).where(Ingredient.id.not_in(ingredients_already_added))
            ingredients = (await session.execute(sql)).scalars().unique().all()

            for ingredient in ingredients:
                sql = insert(IngredientRecipe).values(
                    ingredient_id=ingredient.id,
                    recipe_id=recipe.id
                )
                await session.execute(sql)

            await session.commit()
