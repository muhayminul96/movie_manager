# serializers.py
from rest_framework import serializers
from .models import Movie, Rating, Report

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'released_at', 'duration', 'genre', 'created_by', 'avg_rating', 'total_rating', 'language']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'created_by', 'movie']

    def validate_rating(self, value):
        if not (1.0 <= value <= 5.0):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'movie', 'created_by', 'comment']
