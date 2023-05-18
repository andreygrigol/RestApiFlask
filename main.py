from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

nomes = {"Andrey": {"Idade": 20, "Genero": "Masculino"},
        "Marcelo": {"Idade": 25, "Genero": "Masculino"}}

class Hello(Resource):
    def get(self, nome):
        return nomes[nome]

api.add_resource(Hello, "/helloworld/<string:nome>")

if __name__ == "__main__":
    app.run(debug=True)
