from django.db import models
from django.contrib.auth.models import User

# Create your models here.
RATINGS = (
    ("NC-17", "Adults only"),
    ("R", "Restricted"),
    ("PG-13", "Parents Strongly Cautioned"),
    ("PG", "Parental Guidance"),
    ("G", "General Audiences"),
)


class Opinion(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)


class Comment(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(max_length=4)
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])


class Personnel(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
