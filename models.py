from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
import calendar



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    Area = models.FloatField()
    flowRate = models.FloatField()
    CHOICES = [
    ('Wheat', 'Wheat'),
    ('Rice', 'Rice'),
    ]
    crop = models.CharField(max_length=9,choices=CHOICES)
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    start_date = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    
    def __str__(self) :
        return f"{self.user.username} Profile"