from app.adapter.inmemory_song_repository import InMemorySongRepository
from app.domain.song import Song


def test_song_save():
    song = Song()
    song_repository = InMemorySongRepository()

    assert song.save(song_repository).song_id == song.song_id


def test_song_repository_all():
    song_repository = InMemorySongRepository()
    song1 = Song().save(song_repository)
    song2 = Song().save(song_repository)

    assert set(song_repository.all()) == {song1, song2}


def test_song_repository_total():
    song_repository = InMemorySongRepository()
    Song().save(song_repository)
    Song().save(song_repository)

    assert song_repository.total() == 2