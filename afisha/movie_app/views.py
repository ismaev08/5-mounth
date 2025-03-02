from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *
from movie_app.models import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class DirectorDetailAPIView(RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = DirectorSerializer(data=request.data)
#     if request.method == 'PUT':
#         director.name = serializer.validated_data.get('name')
#         return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#

class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


# @api_view(http_method_names=['GET', 'POST'])
# def directors_list_api_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         list_ = DirectorSerializer(instance=directors, many=True).data
#         return Response(data=list_)
#     elif request.method == 'POST':
#         serializer = DirectorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         name = serializer.validated_data.get('name')
#
#         director = Director.objects.create(
#             name=name,
#         )
#         return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)
#

class MovieDetailAPIView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

#
# @api_view(['GET'])
# def movie_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     data = ReviewValidateSerializer(movie).data
#     return Response(data=data)
#
class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
#
# @api_view(http_method_names=['GET', 'POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         list_ = MovieSerializer(instance=movies, many=True).data
#         return Response(data=list_)
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         duration = serializer.validated_data.get('duration')
#         director = Director.objects.get(id=serializer.validated_data.get('director'))
#
#         movie = Movie.objects.create(
#             title=title,
#             description=description,
#             duration=duration,
#             director=director,
#             director_name=director.name,
#         )
#         return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
#

class ReviewDetailAPIView(RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

# @api_view(['GET'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     data = ReviewValidateSerializer(review).data
#     return Response(data=data)
#
#
class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

# @api_view(http_method_names=['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         list_ = ReviewSerializer(instance=reviews, many=True).data
#         return Response(data=list_)
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         text = serializer.validated_data.get('text')
#         movie = Movie.objects.get(id=serializer.validated_data.get('movie'))
#         grade = serializer.validated_data.get('grade')
#
#         review = Review.objects.create(
#             text=text,
#             movie=movie,
#             grade=grade,
#         )
#         return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
#