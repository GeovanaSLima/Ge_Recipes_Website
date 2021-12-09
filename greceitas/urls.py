from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from greceitas import settings

urlpatterns = [
    path('', include('receitas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
