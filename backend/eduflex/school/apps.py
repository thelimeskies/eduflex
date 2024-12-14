from django.apps import AppConfig


class SchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school'

    def ready(self):
        try:
            import school.signals  # noqa F401
        except ImportError:
