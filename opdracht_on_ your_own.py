import requests
import json

base_url = 'https://pokeapi.co/api/v2/pokemon/'
url_querry = input("Choose your pokemon: ")


r = requests.get(f'{base_url}{url_querry}')

resultName = r.json()["name"]

types = r.json()["types"]
resultType = types[0]["type"]
resultType = resultType["name"]

resultWeight = r.json()["weight"]

resultHeight = r.json()["height"]

resultMoves = r.json()["moves"]
resultMoves = len(resultMoves)

resultId = r.json()["id"]



print(f'name: {resultName}\ntype: {resultType} \nweight: {resultWeight} \nheight: {resultHeight} \nid: {resultId} \nmove amount: {resultMoves}')