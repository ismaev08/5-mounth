from django.urls import path
from .views import MovieListView, DirectorListView, ReviewListView

urlpatterns = [
    path('api/v1/movies/views/', MovieListView.as_view(), name='movie-list'),
    path('api/v1/directors/view/', DirectorListView.as_view(), name='director-list'),
    path('api/v1/review/view/', ReviewListView.as_view(), name='review_list')
]