from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    """Class that holds the schema for the Event table"""

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()


class CustomUser(AbstractUser):
    """Class that overrides User to force emails to be unique"""

    email = models.EmailField(unique=True)
