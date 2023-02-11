import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

from celery import Celery


app = Celery('tasks')
app.config_from_object('django.conf:settings')


@app.task
def add(x, y):
    return x + y