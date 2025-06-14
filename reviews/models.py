from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, "Mínimo 1 estrela"),
            MaxValueValidator(5, "Máximo 5 estrelas"),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie.title} - {self.stars} estrelas"
