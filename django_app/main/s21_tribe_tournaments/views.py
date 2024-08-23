from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.


def main_page(request):
    return redirect(campus_page, "kazan")


def campus_page(request, slug):
    if slug not in ("kazan",):
        raise Http404()
    data = {
        "title": f"{slug.upper()} campus",
        "re_str": slug,
    }
    return render(request, "tournaments/campuses.html", data)


def page_not_found(request, exception):
    data = {"title": "404!"}
    return render(request, "tournaments/error404.html", data)
