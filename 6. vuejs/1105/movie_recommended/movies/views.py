from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.order_by('-pk')[:10]
    context = {
        'movies': movies
    }
    return render(request, 'movies/recommended.html', context)
