from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta

from celery import task

from .models import Logger


@task()
def see_you():
    print("See you in ten seconds!")


@task()
def clean_logger():
    Logger.objects.filter(created__lte=datetime.now()-timedelta(days=7)).delete()
