from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('billboard/', views.billboard, name='billboard'),
    path('wiki/', views.wiki_home, name='wiki_home'),
    path('wiki/<str:song_type>/', views.list_song, name='list_song'),
    path('wiki/<str:song_type>/<str:song_name>/', views.details, name='details'),
    path('blog/', views.blog_home, name='blog_home'),
    path('blog/createBlog/', views.create_blog, name='create_blog'),
    path('blog/<str:blog_name>/<str:person_name>/', views.blog_page, name='blog_page'),
]
