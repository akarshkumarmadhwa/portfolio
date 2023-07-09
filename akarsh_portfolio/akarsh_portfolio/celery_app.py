import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE","akarsh_portfolio.settings")

celery = Celery()

celery.config_from_object("django.conf:settings")
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)