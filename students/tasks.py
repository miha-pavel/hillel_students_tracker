from time import sleep

from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task


@shared_task
def add(a, b):
    print ('ADD Works!')
    sleep(10)
    print(a + b)
    return a + b


@shared_task
def send_email_async(subject, message, student_id):
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, Student.objects.get(id=student_id).email, recipient_list)
