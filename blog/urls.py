from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:blog_topic>/", views.list_blog, name='list_blog'),
]
