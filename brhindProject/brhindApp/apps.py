from django.apps import AppConfig


class BrhindappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brhindApp'

    def ready(self):
        import brhindApp.signals