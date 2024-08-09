from django.urls import path, re_path
from s21_tribe_tournaments import views

urlpatterns = [
    path('', views.main_page),
    re_path(r'^(?P<re_str>[a-z]{3})/', views.tribe),
]