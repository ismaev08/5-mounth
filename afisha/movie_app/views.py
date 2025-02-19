from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializers, DirectorSerializers, ReviewSerializers


@api_view(http_method_names=['GET', 'POST'])
def movie_api_list_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieSerializers(instance=movie, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        # print(request.data)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'POST'])
def director_api_list_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializers(instance=director, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(
            name=name
        )
        return Response(data={'director': director}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET'])
def review_api_list_view(request):
    review = Review.objects.all()
    data = ReviewSerializers(instance=review, many=True).data
    return Response(data=data)

