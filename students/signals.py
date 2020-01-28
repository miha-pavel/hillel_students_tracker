from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Student

# https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
@receiver(pre_save, sender=Student)
# название метода!!
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()

    if instance.id is None:
        import inspect
