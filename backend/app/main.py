from typing import List
from secrets import token_hex

from app.adapter.json_song_repository import JsonSongRepository
from app.domain.song import Song
from app.domain.user import User

from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(30)
app.json.ensure_ascii = False
song_repository = JsonSongRepository()


@app.post("/user/register")
def register() -> User:
    pass


@app.post("/user/login")
def login() -> User:
    pass


@app.post("/song")
def addSong() -> Song:
    data = request.get_json(force=True)
    postedSong = Song()
    postedSong.song_name = data.get('name')
    postedSong.song_description = data.get('description')
    postedSong.song_isPublic = data.get('isPublic')
    postedSong.save(song_repository)
    return jsonify({
        '_id': str(postedSong.song_id),
        'name': postedSong.song_name,
        'description': postedSong.song_description,
        'isPublic': postedSong.song_isPublic
    })


@app.delete("/song")
def deleteSong() -> bool:
    data = request.get_json(force=True)
    deletedSong = Song()
    deletedSong.song_id = data['_id']
    deleted = deletedSong.delete(song_repository)
    return jsonify({
        '_id': str(deletedSong.song_id),
        'name': deletedSong.song_name,
        'description': deletedSong.song_description,
        'isPublic': deletedSong.song_isPublic,
        'deleted': deleted
    })


@app.get("/songs")
def songs() -> List[Song]:
    songList = []
    for song in song_repository.all():
        songList.append({
        '_id': str(song.song_id),
        'name': song.song_name,
        'description': song.song_description,
        'isPublic': song.song_isPublic
    })
    return jsonify(songList)