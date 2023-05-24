import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 53613, "titulo": "Gatos fofos", "views": 7858392},
    {"likes": 5471, "titulo": "Receita de Bolo", "views": 51254},
    {"likes": 67234, "titulo": "Guia de Windows", "views": 7858392},
]

for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.patch(BASE + "video/2", {"views":999})
print(response.json())
