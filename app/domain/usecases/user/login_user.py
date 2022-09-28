from kink import inject

from app.application.graphql_types.dtos import LoginInput
from app.infra.repositories.user import SqlAlchemyUserRepository

@inject
class LoginUserUseCase:
    def __init__(self, user_repository: SqlAlchemyUserRepository) -> None:
        self._user_repo = user_repository

    async def perform(self, login_input: LoginInput):
        print(login_input)
        return {
            'message': 'ok'
        }
