from celery import Celery


app = Celery('tasks', broker='redis://redis:6379/0')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3600 * 4, scan_for_expired_users.s(), name='scan for expired accounts every 4 hours')


@app.task
def scan_for_expired_users():
    """
    TODO
    """
    pass
