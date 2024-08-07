from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect

# Create your views here.


def main_page(request):
    return HttpResponse("<h1>Это тестовая главная страничка турниров</h1>")


def tribe(request, re_str):
    if re_str not in ("kzn", "msk"):
        raise Http404()

    return HttpResponse(f"<h1>Это тестовая страница трайба '{re_str}'</h1>")



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>А такой страницы нет. 404!</h1>")