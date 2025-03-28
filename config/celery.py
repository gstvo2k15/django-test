from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('middleware')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Broker Redis
app.conf.broker_url = 'redis://redis:6379/0'
app.conf.result_backend = 'redis://redis:6379/0'
