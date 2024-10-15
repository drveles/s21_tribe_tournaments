from django.urls import path
from s21_tribe_tournaments import views

urlpatterns = [
    path("", views.main_page, name="tournaments_main"),
    path("<slug:campus_slug>/", views.campus_page, name="campus_page"),
    path("<slug:campus_slug>/<slug:tribe_slug>", views.tribe_page, name="tribe_page"),
]
