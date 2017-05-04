from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    album = models.CharField(max_length = 100)
    year = models.IntegerField(default = 0)
    cover = models.CharField(max_length = 100)

    def __str__(self):
        return self.title