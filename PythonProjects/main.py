import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3202c4a4ac2a8058be69a39b77fabbd4'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
body_pokemons = {
    "name": "Бульбазавр",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = body_pokemons)
print(response_create.text)

message = response_create.json()['message']
print(message)

id = response_create.json()['id']
print(id)


body_new_name = {
    "pokemon_id": id,
    "name": "Pika",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": id
}


response_new_name = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text)
message = response_new_name.json()['message']
print(message)

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
message = response_pokeball.json()['message']
print(message)