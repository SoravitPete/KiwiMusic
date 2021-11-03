from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to Home page of KiwiMusic.")


def detail(request, song_name):
    return HttpResponse("You're looking at %s details." % song_name)


def billboard(request):
    return HttpResponse("You're looking at Billboard. \nThis is ranking for this week.")
