from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import Movie, Rating, Report
from django.contrib.auth.models import User
from .serializers import MovieSerializer,RatingSerializer, ReportSerializer ,UserSerializer
from django.shortcuts import get_object_or_404



class UserView(APIView):
    def get(self, request):
        # Retrieve all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                password=request.data.get('password'),  # Accept password separately
                email=serializer.validated_data.get('email', '')
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')

        # Authenticate user (username could be either email or username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class MovieView(APIView):
    # permission_classes = [AllowAny]
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
            serializer.save(created_by=self.request.user)
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
            print(request.user)
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing rating
        rating = get_object_or_404(Rating, pk=pk)
        # Check if the user is the creator of the movie
        if movie.created_by != request.user:
            return Response({"detail": "You do not have permission to update this movie."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Automatically set the created_by field
        serializer.save(created_by=self.request.user)


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
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


