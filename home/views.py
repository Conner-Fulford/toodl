from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def calendar(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    # Render the HTML template index.html
    return render(request, "calendar.html")


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/calendar")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("/login")
    else:
        # Render the HTML template index.html
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        retype_password = request.POST["retype_password"]
        terms = request.POST.get("terms")
        try:
            if terms is not None and retype_password == password:
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                user.save()
                print(f"User {user.username} created.")
                return redirect("/login")
        except IntegrityError as error:
            error_message = str(error)
            if "unique constraint" in error_message and "username" in error_message:
                messages.info(request, "Username already exits.")
            else:
                messages.info(request, "An error occurred while reigstering.")

    # Render the HTML template index.html
    return render(request, "register.html")


def index(request):
    return render(request, "index.html")
