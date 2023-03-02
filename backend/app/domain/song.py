import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domain.song_repository import SongRepository


@dataclass
class Song:
    song_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    song_owner: str = field(default_factory=lambda: str(uuid.uuid4()))
    song_name: str = field(default_factory=lambda: '')
    song_description: str = field(default_factory=lambda: '')
    song_isPublic: bool = field(default_factory=lambda: False)

    def save(self, song_repository: 'SongRepository'):
        return song_repository.add(self)
    
    def get(self, song_repository: 'SongRepository'):
        return song_repository.get(self)
    
    def delete(self, song_repository: 'SongRepository'):
        return song_repository.delete(self)

    def __hash__(self):
        return hash(self.song_id)