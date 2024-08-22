from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from .models import User, Favorite, Aborted
from django.utils.safestring import mark_safe


class FavoritesInline(admin.TabularInline):
    """Inline in AdminPanel for favorite movies for current user"""
    model = Favorite
    extra = 5
    readonly_fields = ("movie",)


class AbortedsInline(admin.TabularInline):
    """Inline in AdminPanel for ignore movies for current user"""
    model = Aborted
    extra = 5
    readonly_fields = ("movie",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin for User model"""
    list_display = ('id', 'username', 'telegram_id')
    list_display_links = ('id', 'username', 'telegram_id')
    inlines = [FavoritesInline, AbortedsInline]
    fieldsets = (
        ('Информация', {'fields': ('first_name', 'last_name', 'username', 'telegram_id',)}),
    )

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {"url": ("name",)}

    @admin.register(Movie)
    class MovieAdmin(admin.ModelAdmin):
        list_display = ('name', 'category', 'raiting')
        prepopulated_fields = {"url": ("name",)}
        list_display_links = ('name', 'category', 'raiting')
        fieldsets = (
            ('Основное', {'fields': ('name', 'url', 'raiting', 'year', 'description')}),
            ('Жанры', {'fields': ('category', 'genre', 'poster')}),
        )

        def get_image(self, obj):
            return mark_safe(f'<img src={obj.poster.url} width="150" height="120">')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

admin.site.unregister(Group)
admin.site.site_title = "TelePoisk"
admin.site.site_header = "lets see"
