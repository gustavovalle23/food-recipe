from kink import di

from app.domain.contracts.repos.recipe import RecipeRepository
from app.domain.contracts.repos.ingredient import IngredientRepository
from app.domain.contracts.repos.user import UserRepository

from app.infra.repositories.recipe import SqlAlchemyRecipeRepository
from app.infra.repositories.ingredient import SqlAlchemyIngredientRepository
from app.infra.repositories.user import SqlAlchemyUserRepository

def bootstrap():
    di[RecipeRepository] = lambda *args: SqlAlchemyRecipeRepository()
    di[IngredientRepository] = lambda *args: SqlAlchemyIngredientRepository()
    di[UserRepository] = lambda *args: SqlAlchemyUserRepository()
