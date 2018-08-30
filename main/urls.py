from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = "skglist administration"
app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("food/", views.food, name="food"),
    path("drink/", views.drink, name="drink"),
    path("vote/", views.vote, name="vote"),
    path("submit/", views.places_create, name="places_create"),
    path("featured/", views.group_list, name="group_list"),
    path("list/", views.group_create, name="group_create"),
    path("list/<slug:route>/", views.group_redirect, name="group_redirect"),
    path("list/<slug:route>/<slug:group_slug>/", views.group, name="group"),
]
