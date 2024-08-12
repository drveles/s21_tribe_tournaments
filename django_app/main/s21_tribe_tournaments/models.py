from django.db import models

# Create your models here.


class Campuses(models.Model):
    name = models.CharField(max_length=52)
    slug = models.CharField(max_length=52)


class Tournaments(models.Model):
    name = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Tribes(models.Model):
    name = models.CharField(max_length=21)
    slug = models.CharField(max_length=21)
    campus_id = models.ForeignKey(Campuses, on_delete=models.CASCADE)
    master = models.CharField(max_length=52)
    parallel = models.CharField(max_length=21)
    visibility = models.BooleanField(default=False)
    capacity = models.IntegerField(default=0)
    curr_points = models.IntegerField(default=0)
    prev_points = models.IntegerField(default=0)


class Peers(models.Model):
    name = models.CharField(max_length=21)
    campus_id = models.ForeignKey(Campuses, on_delete=models.CASCADE)
    curr_tribe_id = models.ForeignKey(Tribes, on_delete=models.CASCADE, related_name="curr_tribe_id")
    prev_tribe_id = models.ForeignKey(Tribes, on_delete=models.CASCADE, related_name="prev_tribe_id",
                                      null=True, default=None)
    level = models.IntegerField()
    wave = models.CharField(max_length=21)
    curr_points = models.IntegerField(default=0)
    prev_points = models.IntegerField(default=0)
