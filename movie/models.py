from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_num = models.CharField(max_length=13, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genre

class Actor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()
    image = models.ImageField(upload_to='actors/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.country

class Comment(models.Model):
    text = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

class Language(models.Model):
    language = models.CharField(max_length=100)
    
    def __str__(self):
        return self.language
    
class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.DateField()
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='kino/')
    actors = models.ManyToManyField(Actor)
    country = models.ManyToManyField(Country)
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    language = models.ManyToManyField(Language)
    description = models.TextField()
    trailer = models.URLField()
    film = models.FileField()
    
    def __str__(self):
        return self.title