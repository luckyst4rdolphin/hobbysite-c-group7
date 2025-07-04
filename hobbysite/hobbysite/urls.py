from django.contrib import admin
from django.urls import path, include
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('user_management.urls')),
    path('commissions/', include('commissions.urls')),
    path('forum/', include('forum.urls')),
    path('merchstore/', include('merchstore.urls')),
    path('blog/', include('blog.urls')),
    path('wiki/', include('wiki.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)