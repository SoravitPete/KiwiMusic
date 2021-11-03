from django.db import models


class SongName(models.Model):
    song_name = models.CharField(max_length=200)

    def __str__(self):
        return self.song_name


class BillBoard(models.Model):
    billboard = models.CharField(max_length=200)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.billboard


class SongType(models.Model):
    song_type = models.CharField(max_length=200)

    def __str__(self):
        return self.song_type

