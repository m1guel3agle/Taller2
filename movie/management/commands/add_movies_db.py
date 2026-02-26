import json
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Load movies from JSON file into database'

    def handle(self, *args, **kwargs):
        with open('movie/management/commands/movies.json', encoding='utf-8') as file:
            movies = json.load(file)

            for movie in movies[:100]:  # Solo 100 películas
                Movie.objects.create(
    title=movie.get('title', 'No title'),
    description=movie.get('description') or 'No description available',
    genre=movie.get('genre', ''),
    year=movie.get('year'),
    image='movie/images/default.jpg'
)
        self.stdout.write(self.style.SUCCESS('Movies loaded successfully!'))