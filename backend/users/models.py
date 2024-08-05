from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import Movie


class User(AbstractUser):
    telegram_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    movie = models.ManyToManyField(Movie, blank=True)

    class Meta:
        verbose_name = 'Избранное'

class Aborted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="aborted", null=True, blank=True)
    movie = models.ManyToManyField(Movie, blank=True)

    class Meta:
        verbose_name = 'Не предлагать'