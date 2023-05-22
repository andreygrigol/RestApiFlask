from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "nome", type=str, help="Nome do vídeo é obrigatório.", required=True
)
video_put_args.add_argument("views", type=str, help="Views do vídeo")
video_put_args.add_argument("likes", type=str, help="Likes do vídeo")

videos = {}


def abort_not_video_id(video_id):
    if video_id not in videos:
        abort(404, message="Vídeo não encontrado")


def abort_video_id(video_id):
    if video_id in videos:
        abort(409, message="Vídeo já existente")


class Video(Resource):
    def get(self, video_id):
        abort_not_video_id(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_video_id(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_not_video_id(video_id)
        del videos[video_id]
        return "", 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
