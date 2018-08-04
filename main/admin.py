from django.contrib import admin

from . import models


# Place
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "votes", "link", "is_eat", "is_drink", "id")


admin.site.register(models.Place, PlaceAdmin)


# Analytic
class AnalyticAdmin(admin.ModelAdmin):
    list_display = ("ip", "user", "created_at", "path", "querystring")


admin.site.register(models.Analytic, AnalyticAdmin)
