
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_security/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', )),
    path('accounts/', include('django.contrib.auth.urls', )),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

