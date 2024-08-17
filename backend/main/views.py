from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Favorite, Aborted
from .serializers import *
from .utils import _get_or_create_user_from_tg




class RandomMovieView(APIView):
    """Get random movie that not in favorites or ignore list of current user"""
    def get(self, request):
        telegram_id = request.GET.get('telegram_id')
        user = User.objects.get(telegram_id=telegram_id)
        movie = Movie.active.exclude(aborted__user=user).exclude(favorites__user=user)
        random_movie = movie.order_by('?').first()
        serializer = MovieTgSerializer(random_movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrationView(APIView):
    """works when new user click /start on tg bot and check exists him or not"""

    def post(self, request):
        try:
            _get_or_create_user_from_tg(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AddToFavoritesView(APIView):
    """Add movie to user favorite list by telegram_id and movie_id"""
    def post(self, request):

        telegram_id = request.POST.get('telegram_id')
        user = User.objects.get(telegram_id=telegram_id)
        movie_id = request.POST.get('movie_id')
        movie = Movie.active.get(id=movie_id)
        instance = None

        if request.POST.get('list_type') == 'favorites':
            instance = Favorite

        elif request.POST.get('list_type') == 'aborted':
            instance = Aborted
        try:
            inst_list, _ = instance.objects.get_or_create(user=user)
            inst_list.movie.add(movie)

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetFavoriteMoviesView(APIView):
    """Get list of favorite movies by telegram_id"""

    def get(self, request):
        telegram_id = request.GET.get('telegram_id')
        user = User.objects.get(telegram_id=telegram_id)
        favorite = Favorite.objects.get(user=user)
        data = favorite.movie.all().values('name', 'year')
        response = list(data)
        if response:
            return Response(status=status.HTTP_200_OK, data=response)
        return Response(status=status.HTTP_400_BAD_REQUEST)


