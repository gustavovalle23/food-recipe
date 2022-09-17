from sqlalchemy import insert

from app.application.graphql_types.recipe import Ingredient
from app.infra.repositories.ingredient import SqlAlchemyIngredientRepository

async def create_ingredient_use_case(ingredient: Ingredient):
    repo = SqlAlchemyIngredientRepository()
    ingredients = await repo.find_ingredients_by_name(ingredient.name)
    if not ingredients:
        await repo.save(ingredient)
        return True
    return False
