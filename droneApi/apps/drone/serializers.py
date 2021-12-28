from django.db import models
from rest_framework import fields, serializers

from droneApi.apps.medication.models import Medication

from ..medication.serializers import MedicationSerializer
from .models import Drone

class DroneSerializer(serializers.ModelSerializer):
    """ Drone Serializer Class """

    class Meta:
        model = Drone
        fields = ['serial_number', 'model', 'weight_limit', 'battery_capacity', 'state', 'created_at']



class DroneLoadingSerializer(serializers.ModelSerializer):
    """ Drone Loading Serializer Class """
    
    class Meta:
        model = Medication
        fields = ['name', 'weight', 'code', 'image', 'drone']
    
        


class DroneLoadMedicationSerialzer(serializers.ModelSerializer):
    """ Drone Load Serializer Class"""
    drone = DroneSerializer()
    class Meta:
        model = Medication
        fields = ['name', 'weight', 'code', 'image', 'drone']


class DroneBatteryLevelSerializer(serializers.ModelSerializer):
    """ Drone battery level serializer class """
    class Meta:
        model = Drone
        fields = ['battery_capacity']
