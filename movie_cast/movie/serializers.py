from rest_framework import serializers
from movie.models import Movie, Cast


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ["id", "name", "gender", "dob"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "runtime", "language", "tagline"]


class MovieDetailSerializer(serializers.ModelSerializer):
    casts = CastSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "runtime", "language", "tagline", "casts"]
