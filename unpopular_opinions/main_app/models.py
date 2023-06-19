from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


RATINGS = (
    ("NC-17", "Adults only"),
    ("R", "Restricted"),
    ("PG-13", "Parents Strongly Cautioned"),
    ("PG", "Parental Guidance"),
    ("G", "General Audiences"),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.CharField(choices=RATINGS, default=RATINGS[0][0])

    def __str__(self):
      return self.title


class Personnel(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date = models.DateField("posted on")
    content = models.CharField(max_length=500)


class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tldr = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=10000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
      return self.tldr
