from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import exceptions

from .models import Drone
from .serializers import DroneSerializer

class DroneApiView(APIView):
    """ Drone view class """

    serializer_class = DroneSerializer

    def post(self, request):
        """ method to register drones """
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {
                'drone': serializer.data,
                'message': 'Drone registered successfully'
            }

            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': '{}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
