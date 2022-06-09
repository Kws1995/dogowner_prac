from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movies = models.ManyToManyField('Movie')

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'
