from django.http import HttpResponse
from django.shortcuts import render

from .models import SongName, SongType


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


def billboard(request):
    return HttpResponse("You're looking at Billboard. \nThis is ranking for this week.")
