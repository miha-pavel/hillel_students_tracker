from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'

    def ready(self):
        # Импорт делаеться только здесь
        import students.signals
