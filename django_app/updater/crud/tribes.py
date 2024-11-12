from django.utils.text import slugify
from s21_tribe_tournaments.models import Tribes


def create_campus_tribe(name: str, information: dict) -> None:
    Tribes.objects.create(name=name, slug=slugify(name), **information)


def delete_campus_tribe(name: str, slug: str = None) -> None:
    if slug:
        Tribes.objects.filter(slug=slug).delete()
    else:
        Tribes.objects.filter(name=name).delete()
