from .crud.campus import create_campus
from .crud.tribes import create_campus_tribe
from s21_tribe_tournaments.models import Campuses


def create_full_information(campus_name) -> None:
    campuses_tribes = {
        "Kazan": {
            "Aer": "Core",
            "Anglerfish": "Intense",
            "Aqua": "Core",
            "Ignis": "Core",
            "Moray eels": "Intense",
            "Scorpionfish": "Intense",
            "Terra": "Core",
            "Trionics": "Intense",
        }
    }

    if campus_name not in campuses_tribes:
        raise KeyError(f"No campus {campus_name} tribe information to manual creating")

    if Campuses.objects.filter(name=campus_name).exists():
        return

    create_campus(campus_name)
    for tribe_name, tribe_parallel in campuses_tribes[campus_name].items():
        info = {
            "campus": Campuses.objects.get(name=campus_name),
            "parallel": tribe_parallel,
            "visibility": True,
        }
        create_campus_tribe(name=tribe_name, information=info)
