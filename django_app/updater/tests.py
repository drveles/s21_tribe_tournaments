from django.test import TestCase
from django.utils.text import slugify
from s21_tribe_tournaments.models import Campuses
from updater.crud.campus import create_campus, delete_campus


class TestCampusMethods(TestCase):
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
