
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_superuser(request):
    if not User.objects.filter(username='mamun_bepari').exists():
        User.objects.create_superuser('mamun_bepari', 'beparimamun708@gmail.com', 'blog123@')
        return HttpResponse("Superuser created successfully.")
    else: 
        return HttpResponse("Superuser already exists.")

urlpatterns = [
    path('admin_security/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', )),
    path('accounts/', include('django.contrib.auth.urls', )),
    path('make-me-admin/', create_superuser),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

