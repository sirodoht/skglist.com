from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    votes = models.PositiveIntegerField()
    link = models.URLField()
    is_eat = models.BooleanField()
    is_drink = models.BooleanField()
