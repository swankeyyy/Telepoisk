from django.db import models


class CurrentCategory(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category=self.model)


class Category(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=True, max_length=100)
    objects = models.Manager()
    movies = CurrentCategory()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Raiting(models.Model):
    value = models.SmallIntegerField()

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Рейтинг'


class IsActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField(unique=True, max_length=100)
    genre = models.ManyToManyField(to=Genre, verbose_name="Жанр")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='movies',
                                 verbose_name='Категория')
    year = models.SmallIntegerField(default=1980)
    description = models.TextField(default='Описание скоро будет')
    poster = models.FileField(upload_to='posters/', blank=True, null=True)
    raiting = models.ForeignKey(to=Raiting, on_delete=models.SET_NULL, related_name='movies',
                                blank=True, null=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = IsActive()

    def __str__(self):
        return f'{self.name} - {self.year}'

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'

