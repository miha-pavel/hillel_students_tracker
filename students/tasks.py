from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

from celery import shared_task

from .models import Student


@shared_task
def send_email_async(subject, message, student_id):
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, Student.objects.get(id=student_id).email, recipient_list)


@shared_task
def send_signup_email(subject, message, recipient):
    email = EmailMessage(subject, message, to=[recipient])
    email.send()
