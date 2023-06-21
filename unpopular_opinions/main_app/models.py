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

    def get_absolute_url(self):
      return reverse('movie_detail', kwargs={'movie_id': self.id})


class Personnel(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)
    movie_choice = models.CharField('movie', max_length=150)

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('personnel_detail', kwargs={'personnel_id': self.id})

ROLES = (
  ("Actor", "Actor"),
  ("Director", "Director"),
  ("Writer", "Writer"),
  ("Producer", "Producer"),
  ("Casting Director", "Casting Director"),
  ("Cinematographer", "Cinematographer"),
  ("Score", "Score")
)

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tldr = models.CharField('opinion', max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField('explanation', max_length=10000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True)
    person_role = models.CharField('role', choices=ROLES, default=ROLES[0], null=True)
    movie_choice = models.CharField('movie', max_length=150)
    person_choice = models.CharField('cast or crew member', max_length=150, null=True)
    person_movie = models.CharField('movie', max_length=150, null=True)
    
    def __str__(self):
      return self.tldr

    def get_absolute_url(self):
      return reverse('opinion_detail', kwargs={'opinion_id': self.id})

class Comment(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    content = models.CharField('comment', max_length=500)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.title