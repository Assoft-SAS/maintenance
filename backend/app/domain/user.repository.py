import abc

from app.domain.user import User


class UserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def login(self, user: User) -> User:
        raise NotImplementedError
