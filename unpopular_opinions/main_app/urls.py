from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opinion/", views.opinion_index, name="opinion"),
    path("opinion/<int:opinion_id>/", views.opinion_detail, name="opinion_detail"),
    path("opinion/create/", views.OpinionCreate.as_view(), name="opinion_create"),
    path(
        "opinion/<int:pk>/update/", views.OpinionUpdate.as_view(), name="opinion_update"
    ),
    path(
        "opinion/<int:pk>/delete", views.OpinionDelete.as_view(), name="opinion_delete"
    ),
    path("movies/", views.movie_index, name="movies"),
    path("movies/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("movies/create/", views.MovieCreate.as_view(), name="movies_create"),
    path(
        "opinion/<int:opinion_id>/add_comment/", views.add_comment, name="add_comment"
    ),
    path("accounts/signup/", views.signup, name="signup"),
    # URL path name subject to change
    path("api-auth/", include("rest_framework.urls")),
]
