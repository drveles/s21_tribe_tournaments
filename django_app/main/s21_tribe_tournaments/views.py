from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.shortcuts import render
# Create your views here.


def main_page(request):
    data = {
        "title": "Tribe tournaments",
        "items": ["A это", "list", 2, {1, 3}],
    }
    return render(request, "tournaments/index.html", data)


def campus(request, slug):
    if slug not in ("kazan", ):
        raise Http404()
    data = {
        "title": f"{slug.upper()} campus",
        "re_str": slug,
    }
    return render(request, "tournaments/campuses.html", data)


def page_not_found(request, exception):
    data = {
        "title": "404!"
    }
    return render(request, "tournaments/error404.html", data)
