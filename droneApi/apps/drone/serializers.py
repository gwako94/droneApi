from rest_framework import serializers
from .models import Drone

class DroneSerializer(serializers.ModelSerializer):
    """ Drone Serializer class """

    class Meta:
        model = Drone
        fields = '__all__'
