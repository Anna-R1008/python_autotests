import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3202c4a4ac2a8058be69a39b77fabbd4'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
TRAINER_ID = '18371'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_my_trainers():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"]=='Madazar'