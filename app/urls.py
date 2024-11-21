from django.contrib import admin
from django.urls import URLResolver, path, include

from .settings import DEBUG

urlpatterns: list[URLResolver] = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', include('accounts.urls')),
    path('api/pdf/', include('pdf_service.urls')),
]

if DEBUG:
    import debug_toolbar

    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))