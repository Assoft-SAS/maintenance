from tests.fixtures.client import *  # NOQA


def test_get_songs_0(client):
    response = client.get("/songs")
    assert response.status_code == 200
    #assert response.json() == 0


def test_get_songs_1(client):
    client.post("/song")
    response = client.get("/songs")
    assert response.status_code == 200
    #assert response.json() == 1


def test_get_songs_10(client):
    for i in range(1, 10):
        client.post("/song")
    response = client.get("/songs")
    assert response.status_code == 200
    #assert response.json() == 10