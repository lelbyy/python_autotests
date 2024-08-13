import requests

URL= 'https://api.pokemonbattle.ru/v2'
Token = 'f127eae0a5152f10b1a24ef49ccc5e91'
Header = {'Content-Type' : 'application/json',
          'trainer_token' : Token
          }

task1 = requests.post(url = f'{URL}/pokemons', headers=Header, json = {
    "name": "MR chiiuck",
    "photo_id": 1
})

print(task1.text)


task2 = requests.put(url = f'{URL}/pokemons', headers=Header, json = {
    "pokemon_id" : "48489",
    "name": "New chiiuck",
    "photo_id": 2
})

print(task2.text)

task3 = requests.post(url = f'{URL}/trainers/add_pokeball', headers=Header, json = {
    "pokemon_id" : "48489"
})

print(task3.text)