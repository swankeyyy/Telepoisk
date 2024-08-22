from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    """Category of movies like serials, films, etc."""
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    """Genres like actions, drama, triller, etc."""
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class IsActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Movie(models.Model):
    """Single movie model"""
    name = models.CharField(max_length=100, verbose_name='Название')
    url = models.SlugField(unique=True, max_length=100, verbose_name='Slug')
    genre = models.ManyToManyField(to=Genre, verbose_name="Жанр", related_name='movies')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='movies',
                                 verbose_name='Категория')
    year = models.SmallIntegerField(default=1980, verbose_name='Год выпуска')
    description = models.TextField(default='Описание скоро будет', verbose_name='Описание')
    poster = models.FileField(upload_to='posters/', blank=True, null=True, verbose_name='Постер')
    raiting = models.FloatField(default=7, verbose_name='Рейтинг кинопоиска')
    is_active = models.BooleanField(default=True, verbose_name='Опубликовать')

    objects = models.Manager()
    active = IsActive()

    def __str__(self):
        return f'{self.name} - {self.year}'

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'


# custom user models
class User(AbstractUser):
    """Single user model with telegram id"""
    telegram_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Favorite(models.Model):
    """User favorites movies list"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    movie = models.ManyToManyField(Movie, blank=True, related_name="favorites")

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Aborted(models.Model):
    """User Ignore list"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="aborted", null=True, blank=True)
    movie = models.ManyToManyField(Movie, blank=True, related_name="aborted")

    class Meta:
        verbose_name = 'Не предлагать'
        verbose_name_plural = 'Не предлагать'
