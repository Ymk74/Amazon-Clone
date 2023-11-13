from celery import shared_task
import time


@shared_task
def send_emails():
    for x in range(10):
        time.sleep(0.1)
        # send emails
        print(f'Sending Email Number {x}')
