from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toodl.settings')

app = Celery('home')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-for-upcoming-events-every-hour': {
        'task': 'home.tasks.check_for_upcoming_events',
        'schedule': crontab(minute=0, hour='0,12'),  # Adjust the timing as needed
    },
}
