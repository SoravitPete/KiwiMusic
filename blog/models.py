from django.db import models


class BlogTopic(models.Model):
    blog_topic = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_topic
