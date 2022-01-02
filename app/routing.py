from .models import Movie, Genre
from .schemas import MovieSchema, GenreSchema
from flask_restx import fields, reqparse, Resource

from . import api, db

movies_ns = api.namespace('movies')
genres_ns = api.namespace('genres')

parser = reqparse.RequestParser()
parser.add_argument("director_id", type=int)
parser.add_argument("genre_id", type=int)


@movies_ns.route('/')
class ManyMovie(Resource):

    @api.expect(parser)
    def get(self):
        director_id = parser.parse_args()["director_id"]
        genre_id = parser.parse_args()["genre_id"]
        if director_id and genre_id:
            data = Movie.query.filter_by(director_id=director_id, genre_id=genre_id).all()
        elif director_id:
            data = Movie.query.filter_by(director_id=director_id).all()
        elif genre_id:
            data = Movie.query.filter_by(genre_id=genre_id).all()
        else:
            data = Movie.query.all()
        if not data:
            movies_ns.abort(404)
        return MovieSchema(many=True).dump(data)


@movies_ns.route('/<int:id>')
class SingleMovie(Resource):
    def get(self, id):
        obj = Movie.query.get(id)
        if not obj:
            movies_ns.abort(404)
        return MovieSchema().dump(obj)

    def delete(self, id):
        obj = Movie.query.get(id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
        return '', 204


genre = genres_ns.model('Genre', {
    # 'id': fields.Integer(readonly=True),
    'name': fields.String(required=True)
})


@genres_ns.route('/<int:id>')
class SingleGenre(Resource):
    def delete(self, id):
        obj = Genre.query.get(id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
        return '', 204


@genres_ns.route('/')
class ManyGenre(Resource):

    @genres_ns.expect(genre, validate=True)
    @genres_ns.marshal_list_with(genre)
    def post(self):
        obj = Genre(**GenreSchema().load(genres_ns.payload))
        db.session.add(obj)
        db.session.commit()
        return GenreSchema().dump(obj), 201
