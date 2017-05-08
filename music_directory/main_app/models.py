from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Music(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    album = models.CharField(max_length = 100)
    year = models.IntegerField(default = 0)
    cover = models.CharField(max_length = 100, default = 'http://icons.iconarchive.com/icons/iconsmind/outline/512/CD-icon.png')
    lyrics = models.TextField(default = 'Your lyrics here: ')
    video = models.URLField(null = True)

    def __str__(self):
        return self.title