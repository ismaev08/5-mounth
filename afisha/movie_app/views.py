from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializers, DirectorSerializers, ReviewSerializers


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
    data = ReviewSerializers(instance=review, many=True).data
    return Response(data= data)

