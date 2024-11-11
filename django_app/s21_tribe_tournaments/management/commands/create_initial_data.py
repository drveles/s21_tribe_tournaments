from django.core.management.base import BaseCommand
from updater.manual_update import create_full_information


class Command(BaseCommand):
    help = "Creating initial data for campuses"

    def handle(self, *args, **kwargs):
        campus_name = "Kazan"
        try:
            create_full_information(campus_name)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Campus {campus_name} autocreated before running service"
                )
            )
        except KeyError as e:
            self.stdout.write(self.style.ERROR(str(e)))
