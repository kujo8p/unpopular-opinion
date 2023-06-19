from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
<<<<<<< HEAD
    path("opinions/", views.opinion_index, name="opinion"),
    path("opinions/<int:opinion_id>", views.opinion_detail, name="detail"),
    path("opinions/create", views.OpinionCreate.as_view(), name="opinions_create"),
    path("opinions/delete", views.OpinionDelete.as_view(), name="opinions_delete"),
    # path("comments/", views.comment, name="comment"),
    path("comments/create", views.CommentCreate.as_view(), name="comments_create"),
=======
    path("opinion/", views.opinions_index, name="opinion"),
    path('opinion/<int:opinion_id>/', views.opinions_detail, name='detail'),
    # path("opinion/create", views.OpinionCreate.as_view(), name="opinion_create"),
    # path("opinion/<int:pk/update", views.OpinionUpdate.as_view(), name="opinion_update"),
    # path("opinion/<int:pk/delete", views.OpinionDelete.as_view(), name="opinion_delete"),
    # path("comment/", views.comment, name="comment"),
    # path("comment/create", views.CommentCreate.as_view(), name="comment"),
    # path("comment/delete", views.CommentDelete.as_view(), name="delete"),
>>>>>>> 1726bee6a21c98f82b440832833e36485ddc9ba9
]
