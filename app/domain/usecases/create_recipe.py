from sqlalchemy import insert

from app.application.graphql_types.dtos import CreateRecipe
from app.infra.repositories.recipe import SqlAlchemyRecipeRepository

async def create_recipe_use_case(recipe: CreateRecipe):
    repo = SqlAlchemyRecipeRepository()
    await repo.save(recipe)
