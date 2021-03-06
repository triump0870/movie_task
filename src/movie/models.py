from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class Genre(models.Model):
    genre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.genre

class Movie(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, null=False, blank=False)
    release = models.DateField(editable=True)
    imdb_score = models.FloatField()
    popularity = models.IntegerField()
    owner = models.ForeignKey(User, related_name='movies', null=False, blank=False,on_delete=models.CASCADE)


    def __unicode__(self):
        return self.name
