from kink import di

from app.infra.repositories.recipe import SqlAlchemyRecipeRepository
from app.infra.repositories.ingredient import SqlAlchemyIngredientRepository
from app.infra.repositories.user import SqlAlchemyUserRepository

def bootstrap():
    di[SqlAlchemyRecipeRepository] = lambda *args: SqlAlchemyRecipeRepository()
    di[SqlAlchemyIngredientRepository] = lambda *args: SqlAlchemyIngredientRepository()
    di[SqlAlchemyUserRepository] = lambda *args: SqlAlchemyUserRepository()
