from .models import Genre, Category, Movie
from .models import User


def _list_by_genre(genre_url):
    """return queryset of movies by genre"""
    genre = Genre.objects.get(url=genre_url)
    return genre.movies.filter(is_active=True)


def _list_by_category(category_url):
    """return queryset of movies by category"""
    category = Category.objects.get(url=category_url)
    return category.movies.filter(is_active=True)


def _get_or_create_user_from_tg(request):
    """takes data from request from TG bot when user clicked start button
    and create new user if he is not exists"""
    telegram_id = request.POST.get('telegram_id')
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    if not username:
        username = first_name + last_name
    User.objects.get_or_create(telegram_id=telegram_id,
                               username=username, first_name=first_name, last_name=last_name)
