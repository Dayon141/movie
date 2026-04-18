from django.contrib import admin
from .models import CustomUser, Genre, Actor, Country, Comment, Language, Movie

admin.site.register(CustomUser)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Comment)
admin.site.register(Language)
admin.site.register(Movie)