from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('', include('merchstore.urls')),
    path('', include('blog.urls')),
    path('', include('wiki.urls')),
]
