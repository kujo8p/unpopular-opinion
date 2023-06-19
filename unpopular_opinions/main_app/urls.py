from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opinion/", views.opinions_index, name="opinion"),
    path('opinion/<int:opinion_id>/', views.opinions_detail, name='detail'),
    # path("opinion/create", views.OpinionCreate.as_view(), name="opinion_create"),
    # path("opinion/<int:pk/update", views.OpinionUpdate.as_view(), name="opinion_update"),
    # path("opinion/<int:pk/delete", views.OpinionDelete.as_view(), name="opinion_delete"),
    # path("comment/", views.comment, name="comment"),
    # path("comment/create", views.CommentCreate.as_view(), name="comment"),
    # path("comment/delete", views.CommentDelete.as_view(), name="delete"),
]
