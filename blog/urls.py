from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowBlogHome, name='showblog'),
    path('room/<str:blog_name>/<str:person_name>', views.ShowBlogPage, name='showblog'),
]