"""Modules providing django-specific functionality"""
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from home.models import CustomUser


def calendar(request) -> HttpResponse | HttpResponseRedirect:
    """Function to return the calendar view if user is authenticated"""
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "calendar.html")


def login_page(request) -> HttpResponse | HttpResponseRedirect:
    """Function to authenticate user and redirect them to the calendar view"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/calendar")
        messages.info(request, "Invalid username or password")
        return redirect("/login")
    return render(request, "login.html")


def register(request) -> HttpResponse | HttpResponseRedirect:
    """Function to register a user if all checks pass i.e. username is unique"""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        retype_password = request.POST["retype_password"]
        terms = request.POST.get("terms")
        if retype_password != password:
            messages.info(request, "Passwords don't match. Try again.")
        if terms is None:
            messages.info(request, "Must agree to the terms.")
        try:
            if terms is not None and retype_password == password:
                validate_password(password)
                user = CustomUser.objects.create_user(
                    username=username, password=password, email=email
                )
                user.save()
                return redirect("/login")
        except IntegrityError as error:
            error_message = str(error)
            if "unique constraint" in error_message and "username" in error_message:
                messages.info(request, "Username already exits.")
            elif "unique constraint" in error_message and "email" in error_message:
                messages.info(request, "Email already exist.")
            else:
                messages.info(request, "An error occurred while reigstering.")
        except ValidationError:
            messages.info(request, "Password doesn't meet requirements.")
    return render(request, "register.html")


def index(request) -> HttpResponse:
    """Function to render the index view"""
    return render(request, "index.html")


def logout_view(request) -> HttpResponseRedirect:
    """Function to redirect users that logout to the index"""
    logout(request)
    return redirect("index")
