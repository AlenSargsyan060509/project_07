from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="Режиссер")
    bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя актера')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Год рождения')

    def __str__(self):
        return self.name

class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name='Жанр')

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(verbose_name="Описание сюжета")
    
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        verbose_name="Жанры"
    )
    
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
        verbose_name='Актеры'
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies",
        verbose_name='Режиссер',
    )

    def __str__(self):
        return self.title
    
