from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("wiki/<str:blog_topic>/", views.list_blog, name='list_blog'),
    path("wiki/<str:blog_topic>/<str:blog_comment>/", views.details, name='details'),
]