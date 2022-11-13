from django.urls import path

from movie.views import MovieView, MovieDetailView, CastView

app_name = "movie"

urlpatterns = [
    path("movies", MovieView.as_view(), name="movies"),
    path("movies/<int:pk>", MovieDetailView.as_view(), name="movies-detail"),
    path("cast", CastView.as_view(), name="cast"),
]
