from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('billboard/', views.billboard, name='billboard'),
    path('<str:song_name>/', views.detail, name='detail'),
]