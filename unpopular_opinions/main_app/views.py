import os
import uuid
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Opinion, Comment, Movie
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# name possibly subject to change
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def opinion_index(request):
    opinion = Opinion.objects.filter(user=request.user)
    return render(request, "opinions/index.html", {"opinion": opinion})


def opinion_detail(request, opinion_id):
    opinion = Opinion.objects.get(id=opinion_id)
    comments = Comment.objects.all()
    return render(
        request, "opinions/detail.html", {"opinion": opinion, "comments": comments}
    )


def movie_index(request):
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})


class MovieCreate(CreateView):
    model = Movie
    fields = ["title", "release_year"]


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
        # This is how we log a user in via code
        login(request, user)
        return redirect("index")
    else:
        error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
