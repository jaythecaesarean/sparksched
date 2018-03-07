from django.db import models
from django.contrib.auth.models import User
from schedule.models.calendars import Calendar  
from schedule.models.events import Event  
from schedule.models.rules import Rule 


class UserSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
