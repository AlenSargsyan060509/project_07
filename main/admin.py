from django.contrib import admin
from .models import Director, Genre, Actor, Movie

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', "bio"]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']

# 3. Настройка для Актеров
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['birth_date']

# 4. Настройка для Фильмов
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'director']
    list_display_links = ['title']
    search_fields = ['title', 'description']
    list_filter = ['release_year', 'genres']
    filter_horizontal = ['genres', 'actors']