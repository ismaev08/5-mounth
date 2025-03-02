from . import views
from django.urls import path

urlpatterns = [
    path('directors/', views.DirectorListAPIView.as_view()),
    path('movies/', views.MovieListAPIView.as_view()),
    path('reviews/', views.ReviewListAPIView.as_view()),
    path('directors/<int:pk>/', views.DirectorDetailAPIView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailAPIView.as_view()),
    path('movies/<int:pk>/', views.MovieDetailAPIView.as_view()),
    ]