import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

from .models import SongType, BlogName, BlogRoom, SongName


def index(request):
    type_list = SongType.objects.all()
    user = request.user
    context = {
        'type_list': type_list,
        'user': user,
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
    return HttpResponse("You are looking at billboard of this week")


def blog_home(request):
    blog_name = BlogName.objects.all()
    context = {
        'blog_name': blog_name,
    }
    return render(request, 'blog/bloghome.html', context)


def blog_page(request, blog_name, person_name):
    message_all = BlogName.objects.get(blog_name=blog_name)
    message_text = message_all.blogroom_set.all()
    comment_form = CommentForm(data=request.POST)
    new_comment = None
    user = request.user
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.room_name = message_all
        new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'message_text': message_text,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'user': user,
    }
    return render(request, 'blog/blogpage.html', context)


@login_required()
def create_blog(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("title")
        create = BlogName(blog_name=name, creator=user.username)
        create.save()
        return redirect('/home/blog/')
    context = {}
    return render(request, "blog/createblog.html", context)
