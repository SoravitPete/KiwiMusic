from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('Home.urls')),
    path('admin/', admin.site.urls),
]
