from s21_tribe_tournaments.models import Tournaments


def create_or_update_tournament(name: str, information: dict) -> None:
    Tournaments.objects.update_or_create(name=name, **information)


def delete_campus_tournament(name: str) -> None:
    Tournaments.objects.filter(name=name).delete()
