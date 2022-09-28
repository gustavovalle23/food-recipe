import inspect
from typing import List, Optional
from kink import inject
from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload

from app.application.graphql_types.recipe import Recipe as RecipeDto
from app.domain.contracts.repos.user import UserRepository
from app.infra.errors.common import \
    OnlyImplementationsAbstractMethodsAllowedException
from app.infra.models import User


@inject
class SqlAlchemyUserRepository(UserRepository):
    def __init__(self) -> None:
        methods_in_class = inspect.getmembers(
            SqlAlchemyUserRepository, predicate=inspect.isfunction)
        methods_in_super_class = inspect.getmembers(
            UserRepository, predicate=inspect.isfunction)
        if len(methods_in_class) != len(methods_in_super_class)+1:
            raise OnlyImplementationsAbstractMethodsAllowedException
        super().__init__()

    async def find_user_by_username(self, username: str) -> Optional[User]:
        return None
