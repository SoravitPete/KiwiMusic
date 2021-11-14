from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from kiwimusic import views

urlpatterns = [
    path('home/', include('Home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('', lambda request: redirect('home/')),

]
