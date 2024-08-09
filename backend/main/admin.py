from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User, Favorite, Aborted
from django.utils.safestring import mark_safe


class FavoritesInline(admin.TabularInline):
    model = Favorite
    extra = 1
    readonly_fields = ("movie",)


class AbortedsInline(admin.TabularInline):
    model = Aborted
    extra = 1
    readonly_fields = ("movie",)


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'last_login', 'telegram_id')
    list_display_links = ('id', 'username', 'telegram_id')
    inlines = [FavoritesInline, AbortedsInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'raiting')
    prepopulated_fields = {"url": ("name",)}
    list_display_links = ('name', 'category', 'raiting')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="150" height="120">')



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}





admin.site.register(User, CustomUserAdmin)

admin.site.site_title = "TelePoisk"
admin.site.site_header = "lets see"
