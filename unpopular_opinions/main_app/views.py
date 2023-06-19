import os
import uuid
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Opinion, Comment
from django.contrib.auth import login


# name possibly subject to change
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# Function names may change when I know what has been happening on the  Front-end.
def opinions_index(request):
    opinions = Opinion.objects.filter(user=request.user)
    return render(request, "opinions/index.html", {"opinions": opinions})


def opinion_detail(request, opinion_id):
    opinion = Opinion.objects.get(id=opinion_id)
    comment = Comment.objects.all()
    return render(request, 'opinions/detail.html', {
    'opinion': opinion, 'comment': comment
    })

# class OpinionUpdate(LoginRequiredMixin, UpdateView):
#   model = Opinion
#   fields = ['content']

# class OpinionDelete(LoginRequiredMixin, DeleteView):
#   model = Opinion
#   success_url = '/opinion'