from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_celery.settings')
app = Celery('dj_celery')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

# CELERY BEAT Setting:
app.conf.beat_schedule = {
    'send_email_every_day': {
        'task': 'send_email.tasks.send_the_mails',
        'schedule': crontab(hour=17, minute=30),
        #'args': ("anything", "anything")
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))