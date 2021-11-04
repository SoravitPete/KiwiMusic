from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('billboard/', views.billboard, name='billboard'),
    path("wiki/<str:song_type>/", views.list_song, name='list_song'),
    path("wiki/<str:song_type>/<str:song_name>/", views.details, name='details'),
]