import datetime
import json
import random

from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.html import escape
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods, require_safe

from .forms import PlaceForm
from .helpers import get_client_ip, get_group_route, log_analytic
from .models import Group, Membership, Place, Vote


@require_safe
def index(request):
    log_analytic(request)
    places = Place.objects.all().filter(is_enabled=True).order_by("-votes")
    return render(request, "main/index.html", {"places": places})


@require_safe
def food(request):
    log_analytic(request)
    places = Place.objects.all().filter(is_enabled=True, is_eat=True).order_by("-votes")
    return render(request, "main/index.html", {"places": places})


@require_safe
def drink(request):
    log_analytic(request)
    places = (
        Place.objects.all().filter(is_enabled=True, is_drink=True).order_by("-votes")
    )
    return render(request, "main/index.html", {"places": places})


@require_http_methods(["POST"])
def vote(request):
    if request.method == "POST":
        log_analytic(request)
        ip = get_client_ip(request)
        body = request.body.decode("utf-8")
        data = json.loads(body)
        place_id = data["place"]
        place = Place.objects.get(id=place_id)
        # ip_vote = Vote.objects.filter(ip=ip, place=place).order_by("-date").first()
        # if ip_vote:
        #     if ip_vote.date + datetime.timedelta(days=1) > timezone.now():
        #         return JsonResponse(status=400, data={"message": "Error."})
        place.votes += 1
        place.save()
        Vote(ip=ip, place=place).save()
        return JsonResponse(status=200, data={"message": "Success."})


def places_create(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.is_enabled = False
            place.save()
            messages.success(request, "Thank you for your submission!")
            return redirect("main:index")
    else:
        form = PlaceForm()

    return render(request, "main/place_create.html", {"form": form})


@require_http_methods(["POST", "GET", "HEAD"])
def group_create(request):
    places = Place.objects.all().filter(is_enabled=True).order_by("-votes")
    if request.method == "POST":
        body = request.body.decode("utf-8")
        data = json.loads(body)
        new_slug = slugify(data["name"])
        if not new_slug:
            new_slug = "".join(
                random.choices(
                    "abdcefghkmnpqrstuvwxyzABDCEFGHKMNPQRSTUVWXYZ23456789", k=6
                )
            )
        new_group = Group.objects.create(
            name=escape(data["name"]), route=get_group_route(), slug=new_slug
        )
        for place_char in data["places"]:
            place_id = int(escape(place_char))
            place = Place.objects.get(id=place_id)
            Membership.objects.create(group=new_group, place=place)
        group_url = "https://skglist.com/list/" + new_group.route + "/"
        alert_message = (
            'Share your list:<br><a href="' + group_url + '">' + group_url + "</a>"
        )
        messages.success(request, alert_message)
        return JsonResponse(status=200, data={"route": new_group.route})

    return render(request, "main/list_create.html", {"places": places})


@require_safe
def group(request, route, group_slug):
    try:
        group = Group.objects.get(route=route)
    except Group.DoesNotExist:
        raise Http404("List does not exist.")
    if group.slug != group_slug:
        return redirect("main:group", route, group.slug)
    group.visits += 1
    group.save()
    return render(request, "main/list_show.html", {"group": group})


@require_safe
def group_redirect(request, route):
    try:
        group = Group.objects.get(route=route)
    except Group.DoesNotExist:
        raise Http404("List does not exist.")
    return redirect("main:group", route, group.slug)


@require_safe
def group_list(request):
    groups = Group.objects.all().order_by("-visits")
    return render(request, "main/lists.html", {"groups": groups})
