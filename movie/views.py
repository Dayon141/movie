from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from .models import Movie
from .forms import RegisterForm, LoginForm
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    movies = Movie.objects.all()
    query = request.GET.get('q')
    if query:
        movies = movies.filter(
            Q(title__icontains=query) |
            Q(genre__genre__icontains=query) |
            Q(actors__name__icontains=query) |
            Q(country__country__icontains=query) |
            Q(language__language__icontains=query)
        ).distinct()
    else:
        movies = Movie.objects.all().order_by('-id')
    paginator = Paginator(movies, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'movies': page_obj, 'query': query})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')