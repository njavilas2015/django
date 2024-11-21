from pathlib import Path
from dotenv import load_dotenv
from os import getenv

load_dotenv()

BASE_DIR: Path = Path(__file__).resolve().parent.parent

SECRET_KEY: str = getenv("SECRET_KEY", "django-insecure")

AUTH_USER_MODEL: str = "accounts.User"

DEBUG: bool = getenv("DEBUG", True)

ALLOWED_HOSTS: list[str] = []

NATS_URL: str = getenv("NATS_URL", "nats://localhost:4220")

INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
]

REST_FRAMEWORK: dict[str, tuple[str]] = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "app.wsgi.application"

DATABASES: dict[str, dict[str, str]] = {}

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

if not DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": getenv("DB_ENGINE", "django.db.backends.postgresql"),
            "NAME": getenv("DB_NAME"),
            "USER": getenv("DB_USERNAME"),
            "PASSWORD": getenv("DB_PASSWORD"),
            "HOST": getenv("DB_HOST"),
            "PORT": getenv("DB_PORT"),
        }
    }


AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE: str = "en-us"

TIME_ZONE: str = "UTC"

USE_I18N: bool = True

USE_TZ: bool = True

STATIC_URL: str = "static/"

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

EMAIL_BACKEND: str = getenv("EMAIL_BACKEND")
EMAIL_HOST: str = getenv("EMAIL_HOST")
EMAIL_PORT: str = getenv("EMAIL_PORT")
EMAIL_USE_TLS: str = getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER: str = getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD: str = getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL: str = getenv("DEFAULT_FROM_EMAIL")

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

    INTERNAL_IPS: list[str] = [
        # Agrega tu IP local
        "127.0.0.1",
        # O si usas Docker, podrías necesitar algo como esto
        "localhost",
        "0.0.0.0",
    ]
