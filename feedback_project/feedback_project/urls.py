from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include('feedback.urls')),  # Default view to feedback app
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
