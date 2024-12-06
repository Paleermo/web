from django.apps import AppConfig


class AppTwoConfig(AppConfig):
    name = 'app_two'

    def ready(self):
        import app_two.signals
