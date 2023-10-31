from django.urls import include, path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
    path("calendar/", views.calendar, name="calendar"),
]
