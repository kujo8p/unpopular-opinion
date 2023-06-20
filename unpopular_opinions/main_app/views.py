import os
import uuid
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Opinion
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


@login_required
def opinion_detail(request):
    opinion = Opinion.objects.get(id=opinion_id)
    return render(request, "opinions/detail.html", {"opinion": opinion})


def movie_index(request):
    movies = Movie.object.all()


# Server was running before the addition of loginrequr
class OpinionCreate(CreateView, LoginRequiredMixin):
    model = Opinion
    fields = "__all__"


class OpinionUpdate(UpdateView, LoginRequiredMixin):
    model = Opinion
    fields = ["tldr", "content"]


# Might not need this on delete since you have to be logged in to view the opinion.
class OpinionDelete(DeleteView, LoginRequiredMixin):
    model = Opinion
    fields = "__all__"


class CommentCreate(CreateView, LoginRequiredMixin):
    model = Opinion
    fields = "__all__"

    def comment(request):
        pass


class CommentUpdate(UpdateView, LoginRequiredMixin):
    model = Opinion
    fields = ["title", "content"]


class CommentDelete(DeleteView, LoginRequiredMixin):
    model = Opinion
    fields = "__all__"
