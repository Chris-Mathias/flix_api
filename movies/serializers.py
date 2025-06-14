from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError("A data de lançamento deve ser maior que 1888.")
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("O resumo deve ter no máximo 500 caracteres.")
        return value


class MovieDetailSerializer(MovieSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date', 'rating', 'resume', 'actors']

    def get_rating(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 1) if rate else None
