from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializers, DirectorSerializers, ReviewSerializers
from rest_framework import generics



@api_view(http_method_names=['GET'])
def movie_api_list_view(request):
    movie = Movie.objects.all()
    data = MovieSerializers(instance=movie, many=True).data
    return Response(data=data)



@api_view(http_method_names=['GET'])
def director_api_list_view(request):
    director = Director.objects.all()
    data = DirectorSerializers(instance=director, many=True).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_api_list_view(request):
    review = Review.objects.all()
    data = ReviewSerializers(instace=review, many=True).data
    return Response(data=data)

# Представление для вывода списка фильмов с отзывами и средним рейтингом
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Представление для вывода списка режиссеров с количеством фильмов
class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer