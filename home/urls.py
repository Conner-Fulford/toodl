"""Importing necessary django components"""
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
    path("calendar/", views.calendar, name="calendar"),
    path("logout/", views.logout_view, name="logout"),
    path("get_events/", views.get_events, name="get_events"),
]
