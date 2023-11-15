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
    path("import_events/", views.import_events, name="import_events"),
    path("export_events/", views.export_events, name="export_events"),
    path("delete_event/<int:event_id>/", views.delete_event, name="delete_event"),
]
