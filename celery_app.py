import os
import time

from celery import Celery


BROKER_URL = os.getenv(
    "CELERY_BROKER_URL",
    "sqla+sqlite:///celery_queue.db"
)

RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND",
    "db+sqlite:///celery_results.db"
)


celery_app = Celery(
    "tasks",
    broker=BROKER_URL,
    backend=RESULT_BACKEND
)

celery_app.conf.task_track_started = True


@celery_app.task
def send_welcome_email(email):
    time.sleep(10)

    return {
        "email": email,
        "message": "Письмо успешно обработано"
    }
