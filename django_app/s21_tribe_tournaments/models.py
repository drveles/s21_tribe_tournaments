from django.db import models
from django.urls import reverse


class Campuses(models.Model):
    name = models.CharField(max_length=52)
    slug = models.CharField(max_length=52, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tournaments_main", kwargs={"campus_slug": self.slug})


class Tribes(models.Model):
    name = models.CharField(max_length=21)
    slug = models.CharField(max_length=21, unique=True)
    campus = models.ForeignKey(Campuses, on_delete=models.CASCADE)
    parallel = models.CharField(max_length=21)
    visibility = models.BooleanField(default=False)
    master = models.CharField(max_length=52, blank=True)
    capacity = models.IntegerField(default=0)
    curr_points = models.IntegerField(default=0)
    prev_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("campus_page", kwargs={"tribe_slug": self.slug})


class Peers(models.Model):
    name = models.CharField(max_length=21)
    campus = models.ForeignKey(Campuses, on_delete=models.CASCADE)
    curr_tribe = models.ForeignKey(
        Tribes,
        on_delete=models.CASCADE,
        related_name="curr_tribe",
        default=1,
    )
    prev_tribe = models.ForeignKey(
        Tribes,
        on_delete=models.CASCADE,
        related_name="prev_tribe",
        null=True,
        default=None,
    )
    level = models.IntegerField()
    wave = models.CharField(max_length=21)
    curr_points = models.IntegerField(default=0)
    prev_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
