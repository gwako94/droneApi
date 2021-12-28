from django.db import models

from ..drone.models import Drone

class Medication(models.Model):
    """ medication model """
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    code = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    drone = models.ForeignKey(Drone,related_name='drone_load',
                                    blank=True, 
                                    null=True,
                                    on_delete=models.CASCADE)
