from django.db import models


class SongType(models.Model):
    song_type = models.CharField(max_length=200)

    def __str__(self):
        return self.song_type


class SongName(models.Model):
    song_name = models.CharField(max_length=200)
    category = models.ForeignKey(SongType, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name


class BillBoard(models.Model):
    billboard = models.CharField(max_length=200)
    place = models.IntegerField(default=0)

    def __str__(self):
        return self.billboard


class BlogTopic(models.Model):
    blog_topic = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_topic
