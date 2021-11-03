from django.http import HttpResponse
from django.shortcuts import render

from .models import SongName


def index(request):
    song_list = SongName.objects.all()
    context = {
        'song_list': song_list,
    }
    return render(request, 'Home/index.html', context)


def detail(request, song_name):
    return HttpResponse("You're looking at %s details." % song_name)


def billboard(request):
    return HttpResponse("You're looking at Billboard. \nThis is ranking for this week.")
