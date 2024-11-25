from os import listdir, path
from django.urls import include, path as django_path, URLResolver


def clean_path(base_dir: str):
    raw: list[str] = []

    for item in listdir(base_dir):

        if item == "app":
            continue

        raw.append(item)

    return raw


def verify_path(item_path: str, item_path_file: str) -> bool:
    return (
        path.isdir(item_path)
        and not path.islink(item_path)
        and path.isfile(item_path_file)
    )


def discover_apps(base_dir: str) -> list[str]:
    raw: list[str] = []

    for item in clean_path(base_dir):

        item_path: str = path.join(base_dir, item)
        item_path_file: str = path.join(base_dir, item, "apps.py")

        if verify_path(item_path, item_path_file):
            raw.append(item)

    return raw


def discover_route(base_dir: str) -> list[str]:
    raw: list[URLResolver] = []

    for item in clean_path(base_dir):

        item_path: str = path.join(base_dir, item)
        item_path_file: str = path.join(base_dir, item, "urls.py")

        if verify_path(item_path, item_path_file):
            raw.append(django_path("", include(f"{item}.urls")))

    return raw
