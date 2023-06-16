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


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.CharField(max_length=200)


class Opinion(models.Model):
    pass


class Comment(models.Model):
    pass


class Opinion(models.Model):
    pass
