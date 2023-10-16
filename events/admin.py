from django.contrib import admin
from .models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):

    model = Event
    list_display = ['event_name','event_picture','event_date','event_time','event_description']


admin.site.register(Event,EventAdmin)