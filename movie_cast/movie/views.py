from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView

from movie.models import Movie, Cast
from movie.serializers import MovieSerializer, MovieDetailSerializer, CastSerializer


class MovieView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDetailView(RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()


class CastView(CreateAPIView):
    serializer_class = CastSerializer
    queryset = Cast.objects.all()
