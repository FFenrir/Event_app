from django.db import models

# Create your models here.



class Event(models.Model):
    
    event_name = models.CharField(max_length=50)
    event_picture = models.ImageField(blank=True)
    event_date = models.DateField(blank=True)
    event_time = models.TimeField(blank=True)
    event_description = models.TextField(max_length=200)
