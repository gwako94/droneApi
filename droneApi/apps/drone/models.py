from django.db import models
from .helpers import validate_percentage, validate_weight

DRONE_MODEL = (
    ('Lightweight', 'Lightweight'),
    ('Middleweight', 'Middleweight'),
    ('Cruiserweight', 'Cruiserweight'),
    ('Heavyweight', 'Heavyweight'),
)

DRONE_STATE = (
    ('idle', 'IDLE'),
    ('loading', 'LOADING'),
    ('loaded', 'LOADED'),
    ('delivering', 'DELIVERING'),
    ('delivered', 'DELIVERED'),
    ('returning', 'RETURNING'),
)

class Drone(models.Model):
    """Drones model"""
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=50, choices=DRONE_MODEL, default='Lightweight')
    weight_limit = models.FloatField(validators=[validate_weight])
    battery_capacity = models.FloatField(validators=[validate_percentage])
    state=models.CharField(max_length=20, choices=DRONE_STATE, default='idle')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
