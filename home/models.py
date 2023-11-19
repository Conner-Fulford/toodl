from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Class that overrides User to force emails to be unique"""

    email = models.EmailField(unique=True)


class Event(models.Model):
    """Class that holds the schema for the Event table"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    startTime = models.DateTimeField(blank=True)
    endTime = models.DateTimeField(blank=True)

    objects = models.Manager()
