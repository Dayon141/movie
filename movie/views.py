from django.shortcuts import render
from .models import Movie
from django.shortcuts import render, get_object_or_404

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})