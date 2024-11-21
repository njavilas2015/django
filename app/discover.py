from os import listdir, path
from django.urls import include, path as django_path, URLResolver


def discover_apps(base_dir: str) -> list[str]:
    raw: list[str] = []

    for item in listdir(base_dir):

        item_path: str = path.join(base_dir, item)

        item_path_apps: str = path.join(base_dir, item, "apps.py")

        if path.isdir(item_path) and path.isfile(item_path_apps):
            raw.append(f"{item}")

    return raw


def discover_route(base_dir: str) -> list[str]:
    raw: list[URLResolver] = []

    for item in listdir(base_dir):

        item_path: str = path.join(base_dir, item)

        item_path_apps: str = path.join(base_dir, item, "urls.py")

        if path.isdir(item_path) and path.isfile(item_path_apps):
            raw.append(django_path("", include(f"{item}.urls")))

    return raw
