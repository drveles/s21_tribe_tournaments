from django.urls import path, re_path
from s21_tribe_tournaments import views

urlpatterns = [
    path('', views.main_page, name="tournaments_main"),
    path("<slug:slug>/", views.campus, name="campus_page"),
]
