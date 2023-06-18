from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opinions/", views.opinions_index, name="opinions"),
    #     path("opinion/create", views.OpinionCreate.as_view(), name="opinion_create"),
    #     path("opinion/delete", views.OpinionDelete.as_view(), name="opinion_delete"),
    #     path("comment/", views.comment, name="comment"),
    #     path("comment/create", views.CommentCreate.as_view(), name="comment"),
    #     path("comment/delete", views.CommentDelete.as_view(), name="delete"),
]
