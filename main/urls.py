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
    path("list/", views.group_create, name="group_create"),
    path("list/<slug:route>", views.group, name="group"),
]
