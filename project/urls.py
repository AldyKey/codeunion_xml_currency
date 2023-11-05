from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/users/', include('apps.user.urls')),
    path('api/v1/currencies/', include('apps.currency.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
