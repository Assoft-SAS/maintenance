import abc
from typing import List

from app.domain.song import Song


class SongRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, song: Song) -> Song:
        raise NotImplementedError
    
    def get(self, song: Song) -> Song:
        raise NotImplementedError
    
    def update(self, song: Song) -> Song:
        raise NotImplementedError
    
    def delete(self, song: Song) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Song]:
        raise NotImplementedError
