from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Student

# https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
@receiver(pre_save, sender=Student)
# название метода!!
def pre_save_student(sender, instance, **kwargs):
    instance.phone = ''.join([n for n in instance.phone if n.isdigit()])
    instance.email = instance.email.lower()
    instance.first_name = instance.first_name.title()
    instance.last_name = instance.last_name.title()

    if instance.id is None:
        import inspect
