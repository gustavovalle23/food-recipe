from kink import di

from app.infra.repositories.recipe import SqlAlchemyRecipeRepository
from app.infra.repositories.ingredient import SqlAlchemyIngredientRepository

def bootstrap():
    di[SqlAlchemyRecipeRepository] = lambda: SqlAlchemyRecipeRepository()
    di[SqlAlchemyIngredientRepository] = lambda: SqlAlchemyIngredientRepository()
