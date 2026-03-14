
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('blog.api_urls')),
]


# ✅ This is the main URL configuration for the Django project. It inclueds:
# /api/posts/ → Posts API
# /api/comments/ → Comments API
# /api/likes/ → Likes API
# /api/token/ → JWT token obtain
# /api/token/refresh/ → Refresh token