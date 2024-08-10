from rest_framework import serializers
from .models import Category, Movie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'url')


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Movie
        fields = '__all__'

class MovieTgSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Movie
        fields = ('name', 'year', 'genre', 'category', 'description', 'poster', 'id', 'raiting')
