from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opinion/", views.opinions_index, name="opinion"),
    path("opinion/<int:opinion_id>/", views.opinion_detail, name='opinion_detail'),
    path('opinion/type/', views.opinion_type, name='opinion_type'),
    path('opinion/create/', views.OpinionCreate.as_view(), name='opinion_create'),
    path('opinion/create/p/', views.OpinionPersonCreate.as_view(), name='opinion_person_create'),
    path('opinion/add_opinion/', views.add_opinion, name='add_opinion'),
    path('opinion/<int:pk>/update/', views.OpinionUpdate.as_view(), name='opinion_update'),
    path('opinion/<int:pk>/delete', views.OpinionDelete.as_view(), name='opinion_delete'),
    path("movies/", views.movie_index, name="movies"),
    path("movies/<int:movie_id>/", views.movie_detail, name='movie_detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('opinion/<int:opinion_id>/add_comment/', views.add_comment, name='add_comment'),
    path('personnel/', views.personnel_index, name='personnel'),
    path('personnel/<int:personnel_id>/', views.personnel_detail, name='personnel_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
