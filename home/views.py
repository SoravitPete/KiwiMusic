import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import SongName, SongType, BlogName


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
    # url = "https://unsa-unofficial-spotify-api.p.rapidapi.com/artist"
    #
    # querystring = {"id": "1mYsTxnqsietFxj1OgoGbG"}
    #
    # headers = {
    #     'x-rapidapi-host': "unsa-unofficial-spotify-api.p.rapidapi.com",
    #     'x-rapidapi-key': "480217cf18msh7fbc5f033e28fe5p17bafcjsn5bb4f9f93a60"
    # }
    #
    # response = requests.request("GET", url, headers=headers, params=querystring)
    #
    # return HttpResponse(response.text)
    song_type = SongType.objects.get(song_type=song_type)
    song_name = SongName.objects.get(song_name=song_name)
    context = {
        "song_category": song_type,
        "song_name": song_name
    }
    return render(request, 'Home/details.html', context)


def billboard(request):
    # url = "https://top-10-spotify.p.rapidapi.com/"
    #
    # headers = {
    #     'x-rapidapi-host': "top-10-spotify.p.rapidapi.com",
    #     'x-rapidapi-key': "480217cf18msh7fbc5f033e28fe5p17bafcjsn5bb4f9f93a60"
    # }
    # response = requests.request("GET", url, headers=headers)
    # return HttpResponse(response.text)
    # return render(request, "Home/billboard.html", response)
    return HttpResponse("You are looking at billboard of this week")


def blog_home(request):
    blog_name = BlogName.objects.all()
    context = {
        'blog_name': blog_name,
    }
    return render(request, 'blog/bloghome.html', context)


def blog_page(request, blog_name, person_name):
    message = BlogName.objects.get(blog_name=blog_name)
    message_text = message.blogroom_set.all()
    context = {
        'message_text': message_text,
    }
    return render(request, 'blog/blogpage.html', context)


def create_blog(request):
    if request.method == "POST":
        name = request.POST.get("title")
        create = BlogName(blog_name=name)
        create.save()
    context = {}
    return render(request, "blog/createblog.html", context)
