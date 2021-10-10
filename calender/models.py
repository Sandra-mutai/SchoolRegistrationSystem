from django.db import models

class Calender(models.Model):
    event_name=models.CharField(max_length=10)
    event_date=models.DateField()
    event_agenda=models.CharField(max_length=15)
    event_planner=models.CharField(max_length=15)
    event_duration=models.DateField()
    event_venue=models.CharField(max_length=10)
    event_attendees=models.CharField(max_length=4)

 





