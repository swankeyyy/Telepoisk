from django.conf import settings
from rest_framework import status

from main.models import Movie
from .utils import _get_or_create_user_from_tg
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Favorite, Aborted

user_model = settings.AUTH_USER_MODEL


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
        movie = Movie.objects.get(id=movie_id)
        instance = None

        if request.POST.get('list_type') == 'favorite':
            instance = Favorite

        elif request.POST.get('list_type') == 'aborted':
            instance = Aborted
        try:
            list, _ = instance.objects.get_or_create(user=user)
            list.movie.add(movie)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


