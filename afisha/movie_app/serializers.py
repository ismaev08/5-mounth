from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        # fields = '__all__'
        fields = ['name']
        depth = 1


class MovieSerializers(serializers.ModelSerializer):
    director = DirectorSerializers(read_only=True)
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['title', 'description', 'duration', 'director']


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['stars', 'text', 'movie']




