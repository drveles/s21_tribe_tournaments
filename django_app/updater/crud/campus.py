from django.utils.text import slugify
from s21_tribe_tournaments.models import Campuses


def create_campus(name: str) -> None:
    Campuses.objects.create(slug=slugify(name), name=name)

def delete_campus(name: str) -> None:
    Campuses.objects.filter(name=name).delete()
