import strawberry
import typing

from mocks.users import get_users
from schemas.users import User

@strawberry.type
class Query:
	users: typing.List[User] = strawberry.field(resolver=get_users)
