from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_test.settings')

app = Celery('backend_test')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# redis broker
#app.conf.update(
#    BROKER_URL='amqp://guest:127.0.0.1:5672/',
#)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

