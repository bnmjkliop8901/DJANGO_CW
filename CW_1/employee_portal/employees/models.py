from django.db import models

# Create your models here.

class RealTimeWeather(models.Model):
    date = models.DateTimeField()
    weather = models.CharField(max_length=100)
    