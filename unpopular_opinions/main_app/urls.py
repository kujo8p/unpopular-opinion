from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opinions/", views.opinion_index, name="opinion"),
    path("opinions/<int:opinion_id>", views.opinion_detail, name="detail"),
    path("opinions/create", views.OpinionCreate.as_view(), name="opinions_create"),
    path("opinions/delete", views.OpinionDelete.as_view(), name="opinions_delete"),
    # path("comments/", views.comment, name="comment"),
    path("comments/create", views.CommentCreate.as_view(), name="comments_create"),
]
