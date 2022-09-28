import inspect
from typing import List
from kink import inject
from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload

from app.application.graphql_types.recipe import Recipe as RecipeDto
from app.domain.contracts.repos.recipe import RecipeRepository
from app.infra.errors.common import \
    OnlyImplementationsAbstractMethodsAllowedException
from app.infra.models import Ingredient, IngredientRecipe, Recipe, get_session


@inject
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
            sql = select(IngredientRecipe.c.recipe_id).where(
                IngredientRecipe.c.ingredient_id.not_in(ingredient_ids)
            )
            recipes_with_some_ingredient_missing = (await session.execute(sql)).scalars().unique().all()

            sql = select(IngredientRecipe.c.recipe_id)
            recipes_with_ingredient = (await session.execute(sql)).scalars().unique().all()

            sql = select(Recipe).where(
                Recipe.id.not_in(recipes_with_some_ingredient_missing)
            ).where(Recipe.id.in_(recipes_with_ingredient)).options(joinedload(Recipe.ingredients))
            recipes = (await session.execute(sql)).scalars().unique().all()
        return recipes

    async def find_all_recipes(self) -> List[Recipe]:
        async with get_session() as session:
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
            ingredients_already_added = tuple(
                map(lambda ingredient: ingredient.id, recipe.ingredients)
            )

            sql = select(Ingredient).where(
                Ingredient.id.in_(ingredient_ids)
            ).where(Ingredient.id.not_in(ingredients_already_added))
            ingredients = tuple((await session.execute(sql)).scalars().unique().all())

            await multiples_inserts_ingredient_recipe(ingredients, 0, len(ingredients), recipe_id, session)

            await session.commit()


async def multiples_inserts_ingredient_recipe(ingredients: tuple, index_ingredient, qtd_ingredients, recipe_id, session):
    if index_ingredient == qtd_ingredients:
        return

    sql = insert(IngredientRecipe).values(ingredient_id=ingredients[index_ingredient].id,
                                          recipe_id=recipe_id
                                          )
    await session.execute(sql)
    return  await multiples_inserts_ingredient_recipe(ingredients, index_ingredient+1, qtd_ingredients, recipe_id, session)
