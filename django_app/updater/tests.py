from django.test import TestCase
from django.utils.text import slugify
from s21_tribe_tournaments.models import Campuses
from updater.crud.campus import create_campus, delete_campus
from updater.crud.tribes import create_campus_tribe, delete_campus_tribe
from updater.manual_update import create_full_information
from updater.interfaces.auth_school_api import AuthInSchoolAPI
from updater.interfaces.school_api import SchoolAPI


class TestCrudCampusMethods(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.name1 = "Test1"
        self.name2 = "Test2"

    def test_create_campus(self):
        create_campus(self.name1)
        campus = Campuses.objects.get(name=self.name1)
        self.assertEqual(campus.slug, slugify(self.name1))

        create_campus(self.name2)
        campus = Campuses.objects.get(name=self.name2)
        self.assertEqual(campus.name, self.name2)

    def test_delete_campus(self):
        create_campus(self.name1)
        create_campus(self.name2)
        delete_campus(self.name1)
        delete_campus(self.name2)

        with self.assertRaises(Campuses.DoesNotExist):
            Campuses.objects.get(slug=slugify(self.name1))
            Campuses.objects.get(name=self.name2)


class TestCrudTribesMethods(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_all(self):
        campus_name = "Kazan"
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

        for tribe_name, _ in campuses_tribes[campus_name].items():
            delete_campus_tribe(name=tribe_name)


class TestInterfaceAuthScoolAPI(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_token_create(self):

        auth = AuthInSchoolAPI()
        token = auth.get_auth_tocken_to_api()
        self.assertGreater(10, len(token))


class TestInterfaceAuthScoolAPI(TestCase):
    pass


class TestManualCreate(TestCase):
    def test_success(self):
        campus_name = "Kazan"
        create_full_information(campus_name)
        campus = Campuses.objects.get(name=campus_name)
        self.assertEqual(campus.slug, slugify(campus_name))

    def test_failture(self):
        campus_name = "Fail"
        with self.assertRaises(KeyError):
            create_full_information(campus_name)


# needs perf tests for api.
