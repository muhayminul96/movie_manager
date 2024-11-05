from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    released_at = models.DateField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE , related_name='movies')
    avg_rating = models.FloatField(default=0.0)
    total_rating = models.IntegerField(default=0)
    language = models.TextField(max_length=20)

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = models.FloatField(default=0.0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')


    def __str__(self):
        return f"{self.movie.name} - Rating: {self.rating}"
    def clean(self):
        if not (1.0 <= self.rating <= 5.0):
            raise ValidationError("Rating must be between 1 and 5.")

    def save(self, *args, **kwargs):
        # Call clean() to enforce validation before saving
        self.clean()
        super().save(*args, **kwargs)
        self.update_movie_rating()

    def update_movie_rating(self):
        movie = self.movie
        ratings = movie.ratings.all()
        if ratings.exists():
            total_ratings = ratings.count()
            avg_rating = sum(r.rating for r in ratings) / total_ratings
            movie.total_rating = total_ratings
            movie.avg_rating = round(avg_rating, 2)
        else:
            movie.total_rating = 0
            movie.avg_rating = 0.0
        movie.save()


class Report(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reports')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE , related_name='reports')
    comment = models.TextField()
    def __str__(self):
        return movie.name

