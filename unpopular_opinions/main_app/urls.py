from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opinion/", views.opinions_index, name="opinion"),
    path("opinion/<int:opinion_id>/", views.opinion_detail, name='opinion_detail'),
    path("movies/", views.movie_index, name="movies"),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('accounts/signup/', views.signup, name='signup'),
]
