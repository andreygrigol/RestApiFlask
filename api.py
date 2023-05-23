from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class ModeloVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "Video(titulo={titulo}, views={views}, likes={likes})"

resource_fields = {
    'id': fields.Integer,
    'titulo': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}    


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("titulo", type=str, help="Nome do vídeo é obrigatório.", required=True)
video_put_args.add_argument("views", type=int, help="Views do vídeo", required=True)
video_put_args.add_argument("likes", type=int, help="Likes do vídeo", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("titulo", type=str, help="Nome do vídeo é obrigatório.")
video_update_args.add_argument("views", type=str, help="Views do vídeo")
video_update_args.add_argument("likes", type=str, help="Likes do vídeo")


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = ModeloVideo.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Não foi possível encontrar um vídeo com esse ID")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = ModeloVideo.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="ID de vídeo já existente")
            
        video = ModeloVideo(id=video_id, titulo=args['titulo'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = ModeloVideo.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Vídeo não existente, não foi possível atualizar")
            
        if args['titulo']:
            result.titulo = args['titulo']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
            
        db.session.commit()
        
        return result    
    # def delete(self, video_id):
    #     del videos[video_id]
    #     return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
