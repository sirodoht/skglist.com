import json

from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_safe

from .models import Place


@require_safe
def index(request):
    places = Place.objects.all().order_by("-votes")
    return render(request, "main/index.html", {"places": places})


@require_http_methods(["POST"])
def vote(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        data = json.loads(body)
        place_id = data["id"]
        place = Place.objects.get(id=place_id)
        place.votes += 1
        place.save()
        return redirect("main:index")
