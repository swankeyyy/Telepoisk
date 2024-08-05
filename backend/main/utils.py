from .models import Genre, Category, Movie


def _list_by_genre(genre_url):
    """return queryset of movies by genre"""
    genre = Genre.objects.get(url=genre_url)
    return genre.movies.filter(is_active=True)


def _list_by_category(category_url):
    """return queryset of movies by category"""
    category = Category.objects.get(url=category_url)
    return category.movies.filter(is_active=True)


