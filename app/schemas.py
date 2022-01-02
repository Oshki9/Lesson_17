from marshmallow import Schema, fields

class GenreSchema(Schema):
    id = fields.Integer(readonly=True)
    name = fields.String(required=True)


class DirectorSchema(Schema):
    id = fields.Integer(readonly=True)
    name = fields.String(required=True)


class MovieSchema(Schema):
    id = fields.Integer(readonly=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    trailer = fields.String(required=True)
    year = fields.Integer(required=True)
    rating = fields.Integer(required=True)
    genre_id = fields.Integer(required=True)
    director_id = fields.Integer(required=True)
