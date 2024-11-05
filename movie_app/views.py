from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Rating, Report
from .serializers import MovieSerializer,RatingSerializer, ReportSerializer
from django.shortcuts import get_object_or_404

class MovieView(APIView):
    def get(self, request, pk=None):
        # Retrieve a specific movie if pk is provided, otherwise return all movies
        if pk:
            movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new movie
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing movie
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RatingView(APIView):
    def get(self, request, pk=None):
        # Retrieve a specific rating if pk is provided, otherwise return all ratings
        if pk:
            rating = get_object_or_404(Rating, pk=pk)
            serializer = RatingSerializer(rating)
            return Response(serializer.data)
        else:
            ratings = Rating.objects.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new rating
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing rating
        rating = get_object_or_404(Rating, pk=pk)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReportView(APIView):
    def get(self, request, pk=None):
        # Retrieve a specific report if pk is provided, otherwise return all reports
        if pk:
            report = get_object_or_404(Report, pk=pk)
            serializer = ReportSerializer(report)
            return Response(serializer.data)
        else:
            reports = Report.objects.all()
            serializer = ReportSerializer(reports, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new report
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing report
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
