from django.db import models

class Medication(models.Model):
    """ medication model """
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    code = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
