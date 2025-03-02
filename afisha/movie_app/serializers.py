from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, movies):
        return movies.movie_set.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'title description duration director review average_rating'.split()
        # exclude - исключение полей

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum(int(i.grade) for i in reviews if i.grade.isdigit())
            average = sum_reviews / len(reviews)
            return average
        return None

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    grade = serializers.IntegerField()