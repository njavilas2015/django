from django.contrib import admin
from django.urls import URLResolver, path, include
from app.discover import discover_route

from app.settings import DEBUG, BASE_DIR

urlpatterns: list[URLResolver] = [
    path("admin/", admin.site.urls),
    *discover_route(base_dir=BASE_DIR),
]

if DEBUG:
    import debug_toolbar

    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
