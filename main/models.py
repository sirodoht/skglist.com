from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)
    link = models.URLField()
    is_eat = models.BooleanField()
    is_drink = models.BooleanField()
    is_enabled = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Vote(models.Model):
    date = models.DateTimeField(default=timezone.now)
    ip = models.GenericIPAddressField(null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)


class Analytic(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    path = models.CharField(max_length=400, null=True, blank=True)
    querystring = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.ip


class Group(models.Model):
    route = models.CharField(max_length=30)
    slug = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    visits = models.PositiveIntegerField(default=0)
    members = models.ManyToManyField(Place, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.group.slug + "|" + self.place.name
