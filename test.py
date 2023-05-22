import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 53613, "nome": "Gustavo", "views": 7858392},
    {"likes": 5471, "nome": "Receita de Bolo", "views": 51254},
    {"likes": 67234, "nome": "Guia de Windows", "views": 7858392},
]

for i in range(len(data)):
    response = requests.put(BASE + "video/1" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
