from django.db import models

# Create your models here.
class Event(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
