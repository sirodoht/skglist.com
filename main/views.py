import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.html import escape
from django.views.decorators.http import require_http_methods, require_safe

from .helpers import get_client_ip, get_group_route, log_analytic
from .models import Group, Membership, Place, Vote


@require_safe
def index(request):
    log_analytic(request)
    places = Place.objects.all().order_by("-votes")
    return render(request, "main/index.html", {"places": places})


@require_safe
def food(request):
    log_analytic(request)
    places = Place.objects.all().filter(is_eat=True).order_by("-votes")
    return render(request, "main/index.html", {"places": places})


@require_safe
def drink(request):
    log_analytic(request)
    places = Place.objects.all().filter(is_drink=True).order_by("-votes")
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
        ip_vote = Vote.objects.filter(ip=ip, place=place).order_by("-date").first()
        if ip_vote:
            if ip_vote.date + datetime.timedelta(days=1) > timezone.now():
                return JsonResponse(status=400, data={"message": "Error."})
        place.votes += 1
        place.save()
        Vote(ip=ip, place=place).save()
        return JsonResponse(status=200, data={"message": "Success."})


@require_http_methods(["POST", "GET", "HEAD"])
def group_create(request):
    places = Place.objects.all().order_by("-votes")
    if request.method == "POST":
        body = request.body.decode("utf-8")
        data = json.loads(body)
        new_group = Group.objects.create(
            name=escape(data["name"]), route=get_group_route()
        )
        for place_char in data["places"]:
            place_id = int(escape(place_char))
            place = Place.objects.get(id=place_id)
            Membership.objects.create(group=new_group, place=place)
        return JsonResponse(status=200, data={"route": new_group.route})

    return render(request, "main/group_create.html", {"places": places})


@require_safe
def group(request, route):
    group = Group.objects.get(route=route)
    return render(request, "main/group.html", {"group": group})
