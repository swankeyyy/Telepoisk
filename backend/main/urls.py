from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllMoviesView.as_view(), name='all_movies_view'),
    path('categories', views.AllCategoriesView.as_view(), name='all_categories_view'),
    path('genres/<slug:genre_url>', views.AllMoviesView.as_view(), name='by_genres_view'),
    path('categories/<slug:category_url>', views.AllMoviesView.as_view(), name='by_categories_view'),
    path('movie/<slug:movie_url>', views.MovieDetailView.as_view(), name='movie_view'),
]