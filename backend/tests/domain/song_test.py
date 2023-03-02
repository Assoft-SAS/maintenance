import uuid
from app.domain.song import Song


def test_song_existing_song_id():
    song_id = str(uuid.uuid4())
    assert Song(song_id).song_id == song_id


def test_song_defaults():
    song_id = str(uuid.uuid4())
    assert Song().song_id != song_id