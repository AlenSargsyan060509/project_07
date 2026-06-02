from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie
# Create your views here.
class MovieListView(ListView):
    model = Movie
    template_name = "main/movie_list.html"
    context_object_name = "movies"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "main/movie_detail.html"
    context_object_name = "movie"