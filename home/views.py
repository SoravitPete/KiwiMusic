from django.http import HttpResponse
from django.shortcuts import render

from .models import SongName, SongType, BlogTopic


def index(request):
    type_list = SongType.objects.all()
    context = {
        'type_list': type_list,
    }
    return render(request, 'Home/index.html', context)


def list_song(request, song_type):
    song_type = SongType.objects.get(song_type=song_type)
    song_name = song_type.songname_set.all()
    context = {
        "song_type": song_type,
        "list_song": song_name,
    }
    return render(request, 'Home/list.html', context)


def details(request, song_type, song_name):
    song_type = SongType.objects.get(song_type=song_type)
    song_name = SongName.objects.get(song_name=song_name)
    context = {
        "song_category": song_type,
        "song_name": song_name
    }
    return render(request, 'Home/details.html', context)


def billboard(request):
    return HttpResponse("You're looking at Billboard. \nThis is ranking for this week.")


def blog_home(request, blog_topic):
    blog_topic = blog_topic.blogtopic_set.all()

    context = {
        "blog_topic": blog_topic,
    }
    return render(request, 'Home/blog.html', context)


def blog_page(request, blog_topic):
    blog_topic = blog_topic.blogtopic_set.all()

    context = {
        "blog_topic": blog_topic,
    }
    return render(request, 'Home/blog.html', context)
