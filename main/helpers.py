from random import randint

from django.contrib.auth.models import User

from .models import Analytic, Group


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def log_analytic(request):
    new_analytic = Analytic(
        querystring=request.GET.urlencode(),
        ip=get_client_ip(request),
        path=request.path,
    )
    if request.user.is_authenticated:
        new_analytic.user = User.objects.get(id=request.user.id)
    new_analytic.save()


def get_group_route():
    new_route = 0
    while True:
        route_candidate = randint(1000, 9999)
        if not Group.objects.filter(route=route_candidate).exists():
            new_route = route_candidate
            break
    return str(new_route)
