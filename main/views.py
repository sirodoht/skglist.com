import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_safe

from .helpers import get_client_ip, log_analytic
from .models import Place, Vote


@require_safe
def index(request):
    log_analytic(request)
    places = Place.objects.all().order_by("-votes")
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
            if ip_vote.date < timezone.now():
                return JsonResponse(status=400, data={"message": "Error."})
        place.votes += 1
        place.save()
        Vote(ip=ip, place=place).save()
        messages.success(request, "Vote registered")
        return JsonResponse(status=200, data={"message": "Success."})
