import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Task.settings')

import django
django.setup()
from users.models import Event

app = Celery('Task')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
try:
    res = Event.objects.filter().order_by('-id')[0]
    app.conf.beat_schedule = {
        'clean': {
            'task': 'users.tasks.cleanup',
            'schedule': 16.0,
            'start_time': res.datetime,
        }
    }
except IndexError:
    pass
