from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bidgenius.settings')

app = Celery('bidgenius')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace = 'CELERY')

#Celery beat settings
# app.conf.beat_schedule={
#     'send-email-every-day-at-12pm': {
#         'task': 'auctions.tasks.send_mail_function',
#         'schedule': crontab(hour=11, minute=29),
#         # 'args': ('Your Subject', 'Your message body', ['recipient@example.com']),
#     },
# }

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")