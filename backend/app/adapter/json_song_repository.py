import json
from typing import List

from app.domain.song import Song
from app.domain.song_repository import SongRepository


class JsonSongRepository(SongRepository):
    def __init__(self):
        storeFile = open('songs.json', mode="r", encoding="utf-8")
        self.store = []
        for store in json.load(storeFile):
            importedSong = Song()
            importedSong.song_id = store.get('song_id')
            importedSong.song_name = store.get('song_name')
            importedSong.song_description = store.get('song_description')
            importedSong.song_isPublic = store.get('song_isPublic')
            self.store.append(importedSong)
        storeFile.close()

    def add(self, song: Song) -> Song:
        self.store.append(song)
        with open('songs.json', 'w') as f:
            desStore = []
            for song in self.store:
                desStore.append({
                    'song_id': str(song.song_id),
                    'song_name': song.song_name,
                    'song_description': song.song_description,
                    'song_isPublic': song.song_isPublic
                })
            json.dump(desStore, f)
        return song
    
    def get(self, currentSong: Song) -> Song:
        current = {}
        for song in self.store:
            if str(song.song_id) == currentSong.song_id:
                current = song
                break
        return current

    def all(self) -> List[Song]:
        return self.store

    def delete(self, currentSong: Song) -> bool:
        with open('songs.json', 'w') as f:
            desStore = []
            flag = False
            aux = 0
            delKey = 0
            for song in self.store:
                if song.song_id == currentSong.song_id:
                    flag = True
                    delKey = aux
                else:
                    desStore.append({
                        'song_id': str(song.song_id),
                        'song_name': song.song_name,
                        'song_description': song.song_description,
                        'song_isPublic': song.song_isPublic
                    })
                aux += 1
            json.dump(desStore, f)
        if flag:
            del self.store[delKey]
        return flag