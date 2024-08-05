from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from .models import Category, Movie, Genre
from .serializers import *
from .utils import _list_by_genre, _list_by_category


class AllMoviesView(APIView):
    """View for get all movies"""

    def get(self, request, genre_url=None, category_url=None):
        if genre_url:
            movies = _list_by_genre(genre_url)
        elif category_url:
            movies = _list_by_category(category_url)
        else:
            movies = Movie.active.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class AllCategoriesView(APIView):
    """Returns list of categories"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Returns info about chosen movie"""

    def get(self, request, movie_url):
        """return movie by url"""
        try:
            movie = Movie.objects.get(url=movie_url)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

        except Movie.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class RandomMovieView(APIView):

    def get(self, request):
        telegram_id = request.GET.get('telegram_id')
        user = User.objects.get(telegram_id=telegram_id)
        movie = Movie.objects.exclude(favorites__user=user) & Movie.objects.exclude(aborted__user=user)
        random_movie = movie.order_by('?').first()
        serializer = MovieTgSerializer(random_movie)

        print(user)
        return Response(serializer.data, status=status.HTTP_200_OK)