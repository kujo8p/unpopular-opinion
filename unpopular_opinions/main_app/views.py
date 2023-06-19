import os
import uuid
import boto3
from django.shortcuts import render, redirect
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
    return render(request, "opinion/index.html", {"opinion": opinions})


def opinion_detail(request):
    opinion = Opinion.objects.get(id=opinion_id)
    return render(request, "opinion/detail.html", {"opinion": opinion})


class OpinionCreate(CreateView):
    model = Opinion
    fields = "__all__"


class OpinionUpdate(UpdateView):
    model = Opinion
    fields = ["tldr", "content"]


class OpinionDelete(DeleteView):
    model = Opinion
    fields = "__all__"


class CommentCreate(CreateView):
    model = Opinion
    fields = "__all__"

    def comment(request):
        pass


class CommentUpdate(UpdateView):
    model = Opinion
    fields = ["title", "content"]


class CommentDelete(DeleteView):
    model = Opinion
    fields = "__all__"
