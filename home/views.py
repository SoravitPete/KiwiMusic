from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to Home page of KiwiMusic.")
