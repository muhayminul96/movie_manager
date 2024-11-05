from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', views.MovieView.as_view(), name='movie-detail-update'),
    path('ratings/', views.RatingView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', views.RatingView.as_view(), name='rating-detail-update'),
    path('reports/', views.ReportView.as_view(), name='report-list-create'),
    path('reports/<int:pk>/', views.ReportView.as_view(), name='report-detail-update'),
    path('login/', views.LoginView.as_view(), name='login'),
]
