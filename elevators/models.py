from django.db import models

class Elevator(models.Model):
    current_floor = models.IntegerField(default=1)
    is_moving = models.BooleanField(default=False)
    is_operational = models.BooleanField(default=True)
    is_door_open = models.BooleanField(default=False)