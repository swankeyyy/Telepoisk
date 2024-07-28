from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'raiting')
    prepopulated_fields = {"url": ("name",)}
    list_display_links = ('name', 'category', 'raiting')
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    pass

