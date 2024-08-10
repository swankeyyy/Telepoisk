from django.urls import path
from . import views

urlpatterns = [
    path('random_movie/', views.RandomMovieView.as_view(), name='random_movie_view'),
    path("register/", views.RegistrationView.as_view(), name="register"),
    path('add_to_list/', views.AddToFavoritesView.as_view(), name="add_to_favorite"),
    path('get_favorites/', views.GetFavoriteMoviesView.as_view(), name="get_favorites"),
]
