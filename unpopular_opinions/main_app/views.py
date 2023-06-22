import os
import uuid
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Opinion, Movie, Comment, User, Personnel
from .forms import CommentForm, OpinionForm, OpinionFormPerson
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
    opinion = Opinion.objects.all()
    return render(request, "opinions/index.html", {"opinions": opinions, 'opinion': opinion})


def opinion_detail(request, opinion_id):
    opinion = Opinion.objects.get(id=opinion_id)
    comments = Comment.objects.all()
    comment_form = CommentForm()
    return render(request, 'opinions/detail.html', {
    'opinion': opinion, 'comments': comments, 'comment_form': comment_form
    })

def personnel_index(request):
    personnel = Personnel.objects.all()
    return render(request, "personnel/index.html", {"personnel": personnel})


def personnel_detail(request, personnel_id):
    person = Personnel.objects.get(id=personnel_id)
    return render(request, 'personnel/detail.html', {
    'person': person})

def opinion_type(request):
    return render(request, "opinions/type.html")

class OpinionCreate(CreateView):
    model = Opinion
    form_class = OpinionForm

def load_movies(request):
    personnel_id = request.GET.get('person')
    movies = Personnel.objects.get(id=personnel_id).movies.all().order_by('title')
    return render(request, 'opinions/person_movie_dropdown.html', {'movies': movies})

class OpinionPersonCreate(CreateView):
    model = Opinion
    form_class = OpinionFormPerson
    template_name_suffix = '_person_form'

class OpinionUpdate(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ['tldr', 'content']

class OpinionDelete(LoginRequiredMixin, DeleteView):
    model = Opinion
    success_url = '/opinion'

def movie_index(request):
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {
        'movie': movie
    })

class MovieCreate(CreateView):
    model = Movie
    fields = ["title", "release_year"]

def add_opinion(request):
    form = OpinionForm(request.POST)
    if form.is_valid():
        new_opinion = form.save(commit=False)
        new_opinion.user_id = request.user.id
        new_opinion.save()
    return redirect('opinion')

def add_person_opinion(request):
    form = OpinionFormPerson(request.POST)
    if form.is_valid():
        new_opinion = form.save(commit=False)
        new_opinion.user_id = request.user.id
        new_opinion.save()
    return redirect('opinion')

def add_comment(request, opinion_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.opinion_id = opinion_id
        new_comment.user_id = request.user.id
        new_comment.save()
    return redirect('opinion_detail', opinion_id=opinion_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
        # This is how we log a user in via code
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)