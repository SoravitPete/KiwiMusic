import spotipy
from django.utils import timezone
from spotipy.oauth2 import SpotifyClientCredentials
from django.shortcuts import render, redirect
from .forms import CommentForm, Comment
from django.contrib.auth.decorators import login_required

from .models import SongType, BlogName, SongName


def index(request):
    type_list = SongType.objects.all()
    user = request.user
    context = {
        'type_list': type_list,
        'user': user,
    }
    return render(request, '../templates/index.html', context)


def list_song(request, song_type):
    song_type = SongType.objects.get(song_type=song_type)
    song_name = song_type.songname_set.all()
    context = {
        "song_type": song_type,
        "list_song": song_name,
    }
    return render(request, '../templates/list.html', context)


def details(request, song_type, song_name):
    song_type = SongType.objects.get(song_type=song_type)
    song_name = SongName.objects.get(song_name=song_name)
    song_details = song_name.songdetails_set.all()
    comment_form = Comment(data=request.POST)
    new_comment = None
    user = request.user
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.song_name = song_name
        new_comment.user = user
        new_comment.save()
    else:
        comment_form = Comment()

    context = {
        "song_category": song_type,
        "song_name": song_name,
        "song_details": song_details,
        "new_comment": new_comment,
        "comment_form": comment_form,
        'user': user,
    }
    return render(request, '../templates/details.html', context)


def billboard(request):
    if request.method == 'POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id='36bcf4008345482db62c9dcdbc23cb20',
                                                                client_secret='a75d83de14284a65864d87cab8f0af07', ))
        results = spotify.artist_top_tracks(artist_uri)
        final_result = results['tracks'][:10]
        return render(request, '../templates/billboard.html', {"results": final_result})
    else:
        return render(request, '../templates/billboard.html', )


def wiki_home(request):
    if request.method == 'POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id='36bcf4008345482db62c9dcdbc23cb20',
                                                                client_secret='a75d83de14284a65864d87cab8f0af07', ))
        results = spotify.artist_albums(artist_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = spotify.next(results)
            albums.extend(results['items'])

        return render(request, '../templates/wiki.html', {"albums": albums})
    else:
        return render(request, '../templates/wiki.html', )


def blog_home(request):
    blog_name = BlogName.objects.all()
    context = {
        'blog_name': blog_name,
    }
    return render(request, '../templates/bloghome.html', context)


def blog_page(request, blog_name, person_name):
    message_all = BlogName.objects.get(blog_name=blog_name)
    message_text = message_all.blogroom_set.all()
    comment_form = CommentForm(data=request.POST)
    new_comment = None
    user = request.user
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.room_name = message_all
        new_comment.user = user
        new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'message_text': message_text,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'user': user,
    }
    return render(request, '../templates/blogpage.html', context)


@login_required()
def create_blog(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("title")
        create = BlogName(blog_name=name, creator=user.username, pub_date=timezone.now())
        create.save()
        return redirect('/home/blog/')
    context = {}
    return render(request, "../templates/createblog.html", context)
