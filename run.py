from app import create_app, db
from app.models import Director, Genre, Movie
from app.schemas import DirectorSchema, GenreSchema, MovieSchema

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Director': Director, 'Genre': Genre, 'Movie': Movie,
        'DirectorSchema': DirectorSchema, 'GenreSchema': GenreSchema, 'MovieSchema': MovieSchema
    }


if __name__ == '__main__':
    app.run()