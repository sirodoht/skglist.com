from django.contrib import admin

from . import models


# Place
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "votes",
        "link",
        "is_eat",
        "is_drink",
        "id",
        "is_enabled",
    )


admin.site.register(models.Place, PlaceAdmin)


# Analytic
class AnalyticAdmin(admin.ModelAdmin):
    list_display = ("ip", "user", "created_at", "path", "querystring")


admin.site.register(models.Analytic, AnalyticAdmin)


# Vote
class VoteAdmin(admin.ModelAdmin):
    list_display = ("ip", "date", "place")


admin.site.register(models.Vote, VoteAdmin)


# Group
class GroupAdmin(admin.ModelAdmin):
    list_display = ("route", "name", "slug", "created_at", "visits")


admin.site.register(models.Group, GroupAdmin)


# Membership
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "place")


admin.site.register(models.Membership, MembershipAdmin)
