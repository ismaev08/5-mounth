from rest_framework import serializers
from .models import Movie, Director, Review


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['title', 'description', 'duration', 'director',]


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        # fields = '__all__'
        fields = ['name', 'category', 'hash_tags']
        depth = 1


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie', 'STARS']




