from django.db import models
from django.contrib.auth.models import User

# Create your models here.
RATINGS = (
    ("Adults only", "NC-17"),
    ("Restricted", "R"),
    ("Parents Strongly Cautioned", "PG-13"),
    ("Parental Guidance", "PG"),
    ("Parental Guidance", "PG"),
)


class Movie(models.model):
    RATINGS
    title = models.CharField(max_length=100)
    rating = models.CharField()


class Opinion(models.model):
    pass


class Comment(models.model):
    pass


class Opinion(models.model):
    pass
