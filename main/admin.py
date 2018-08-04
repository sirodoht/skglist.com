from django.contrib import admin

from . import models


# Place
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "votes", "link", "is_eat", "is_drink", "id")


admin.site.register(models.Place, PlaceAdmin)
