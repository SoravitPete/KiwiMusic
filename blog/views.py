from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html', {})


def ShowBlogHome(request):
    return HttpResponse("blog Home")


def ShowBlogPage(request, blog_name, person_name):
    # return render(request,"chat_screen.html",{'room_name':room_name,'person_name':person_name})
    return HttpResponse("Blog page " + blog_name + "" + person_name)
