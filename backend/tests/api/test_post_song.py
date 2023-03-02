from secrets import token_hex
from random import getrandbits

from tests.fixtures.client import *  # NOQA


def test_post_song(client):
    response = client.post(
        "/song",
        data={
            'name': token_hex(8),
            'description': token_hex(20),
            'isPublic': getrandbits(1)
        }
    )
    assert response.status_code == 200