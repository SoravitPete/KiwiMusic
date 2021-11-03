from django.http import HttpResponse
from django.shortcuts import render

from .models import SongName, SongType


def index(request):
    type_list = SongType.objects.all()
    context = {
        'type_list': type_list,
    }
    return render(request, 'Home/index.html', context)


def detail(request, song_type):
    return HttpResponse("You're looking at %s details." % song_type)


def billboard(request):
    return HttpResponse("You're looking at Billboard. \nThis is ranking for this week.")
