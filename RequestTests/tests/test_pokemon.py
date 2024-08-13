import requests
import pytest

URL= 'https://api.pokemonbattle.ru/v2'
Token = 'f127eae0a5152f10b1a24ef49ccc5e91'
Header = {'Content-Type' : 'application/json',
          'trainer_token' : Token
          }
Trainer_ID = 5266

def test_status_code():
    response1 = requests.get(url = f'{URL}/trainers')
    assert response1.status_code == 200

def test_my_id():
    response2 = requests.get(url = f'{URL}/trainers?trainer_id={Trainer_ID}')
    assert response2.json()["data"][0]["trainer_name"] == 'lelby'

