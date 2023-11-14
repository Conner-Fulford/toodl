"""Modules providing django-specific functionality"""
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from home.models import CustomUser, Event
from .forms import EventForm


@login_required
def calendar(request) -> HttpResponse | HttpResponseRedirect:
    """Function to return the calendar view if user is authenticated"""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.user = request.user
            new_event.save()
            form = EventForm()

    else:
        form = EventForm()

    events = Event.objects.filter(user=request.user)
    return render(request, "calendar.html", {"events": events, "form": form})


@login_required
def get_events(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"})

    events = Event.objects.filter(user=request.user)
    event_data = []
    for event in events:
        event_data.append(
            {
                "id": event.id,
                "title": event.title,
                "description": event.description,
                "start": event.startTime,
                "end": event.endTime,
            }
        )
    return JsonResponse(event_data, safe=False)


def delete_event(request, event_id):
    if "event_id" in request.POST:
        event = get_object_or_404(Event, pk=event_id)
        event.delete()
    return redirect("calendar")


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