from s21_tribe_tournaments.models import Tribes


def create_campus_tribe(tribe_slug: str, information: dict) -> None:
    Tribes.objects.create(slug=tribe_slug, **information)


def delete_campus_tribe(slug: str) -> None:
    Tribes.objects.filter(slug=slug).delete()
