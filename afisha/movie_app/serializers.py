from rest_framework import serializers
from movie_app.models import Movie, Director, Review


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['title', 'description', 'duration', 'director']


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        # fields = '__all__'
        fields = ['name']

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ['text', 'movie']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Список отзывов
    rating = serializers.SerializerMethodField()  # Средний рейтинг

    class Meta:
        model = Movie
        fields = ['id', 'title', 'reviews', 'rating']

    def get_rating(self, obj):
        # Рассчитываем средний рейтинг всех отзывов
        reviews = obj.reviews.all()
        if reviews:
            total_stars = sum(review.stars for review in reviews)
            return total_stars / len(reviews)
        return 0

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']