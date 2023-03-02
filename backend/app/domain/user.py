import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domain.user_repository import UserRepository


@dataclass
class User:
    user_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_email: str = field(default_factory=lambda: '')
    user_password: str = field(default_factory=lambda: '')

    def register(self, user_repository: 'UserRepository'):
        return user_repository.register(self)
    
    def login(self, user_repository: 'UserRepository'):
        return user_repository.login(self)

    def __hash__(self):
        return hash(self.user_id)