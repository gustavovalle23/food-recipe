import abc
from typing import Optional
from app.infra.models import User

from app.infra.shared.utils import subclass_hook_return


class UserRepository(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return subclass_hook_return(subclass)

    @abc.abstractmethod
    async def find_user_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError
