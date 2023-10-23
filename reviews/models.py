from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(
                0, 'A avaliação não pode ser inferior a 0 estrelas'),
            MaxValueValidator(
                5, 'A avaliação não pode ser superior a 5 estrelas'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie