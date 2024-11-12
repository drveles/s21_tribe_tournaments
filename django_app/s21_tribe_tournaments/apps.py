from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command


class S21TribeTournamentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "s21_tribe_tournaments"

    def ready(self):
        post_migrate.connect(self.create_initial_data)

    def create_initial_data(self, **kwargs):
        call_command('create_initial_data') 
