from django.apps import AppConfig


class TeachersConfig(AppConfig):
    name = 'teachers'

    def ready(self):
        # Импорт делаеться только здесь
        import teachers.signals
