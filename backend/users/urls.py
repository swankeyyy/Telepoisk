from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("register/", views.RegistrationView.as_view(),name="register"),
    path('add_to_favorite/', views.AddToFavoritesView.as_view(), name="add_to_favorite"),
]