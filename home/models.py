from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
