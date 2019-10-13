from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # It will help to initialise signals.py file.
    def ready(self):
        from . import signals
