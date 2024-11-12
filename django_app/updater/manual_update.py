from .crud.campus import create_campus
from .crud.tribes import create_campus_tribe
from .auto_update import update_tribe_members, update_peers_rank
from .interfaces.school_api import SchoolAPI
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
    school_api = SchoolAPI()
    for tribe_name, tribe_parallel in campuses_tribes[campus_name].items():
        info = {
            "campus": Campuses.objects.get(name=campus_name),
            "parallel": tribe_parallel,
            "visibility": True,
        }
        create_campus_tribe(name=tribe_name, information=info)

        members = school_api.get_campus_tribes_memebers(campus_name)
        update_tribe_members()

        # get_peers_rank_from_api()
        # update_peers_rank()
