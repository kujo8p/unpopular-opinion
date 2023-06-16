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
    rating = models.CharField(max_length=5)


class Opinion(models.Model):
  title = models.CharField(max_length=150)
  content = models.CharField(max_length=500)
  release_year = 


class Comment(models.Model):
    pass


class Personnel(models.Model):
  role = models.CharField(max_length=50)
  name = models.CharField(max_length=100)
    pass
