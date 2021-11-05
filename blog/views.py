from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogTopic, BlogComment


def index(request):
    type_list = SongType.objects.all()
    context = {
        'type_list': type_list,
    }
    return HttpResponse("Welcome to blog page.")


def list_blog(request, blog_topic):
    blog_topic = BlogTopic.objects.get(blog_topic=blog_topic)
    context = {
        "blog_topic": blog_topic,
    }
    return HttpResponse("List of blog.")


def details(request, blog_topic, blog_comment):
    blog_topic = BlogTopic.objects.get(blog_topic=blog_topic)
    context = {
        "blog_topic": blog_topic,
    }
    return HttpResponse("blog details")
