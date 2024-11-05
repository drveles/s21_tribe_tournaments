from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Campuses

# Create your views here.


def main_page(request):
    return redirect(campus_page, "kazan")


def campus_page(request, campus_slug):
    campus = get_object_or_404(Campuses, slug=campus_slug)

    data = {
        "title": f"{campus_slug.upper()} campus",
        "re_str": campus_slug,
    }
    return render(request, "tournaments/campuses.html", data)


def tribe_page(request, campus_slug, tribe_slug):
    campus = get_object_or_404(Campuses, slug=campus_slug)
    return redirect(campus_page, campus_slug)


def page_not_found(request, exception):
    data = {"title": "404!"}
    return render(request, "tournaments/error404.html", data)
