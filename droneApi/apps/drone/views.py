from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Drone
from ..medication.models import Medication

from .serializers import ( 
    DroneBatteryLevelSerializer,
    DroneLoadMedicationSerialzer, 
    DroneLoadingSerializer, 
    DroneSerializer 
)

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

            return Response(res, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': '{}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """ Method to get all available drones """

        # Drone is available if its state is idle
        state = 'idle'
        query_set =  Drone.objects.filter(state=state)
        serializer = self.serializer_class(query_set, many=True)
        res = {
            'Drones': serializer.data,
            'message': 'Succesfully fetched all available drones'
        }

        return Response(res, status=status.HTTP_200_OK)



class DroneLoadingView(APIView):
    """ Drone loading view class """
    serializer_class = DroneLoadingSerializer
    
    def post(self, request, serial_number):

        try:
            drone = Drone.objects.get(serial_number=serial_number)
            data = request.data
            if drone.battery_capacity < 25.0 or data['weight'] > drone.weight_limit:
                return Response({'message': 'Cannot load drone, battery level below 25 or drone\'s weight limit excedeed'})
            data['drone'] = drone.id
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            drone.state = 'loaded'
            res = {
                'Medication': serializer.data,
                'message': 'Successfully loaded drone with medication'
            }
            return Response(res, status=status.HTTP_200_OK)

        except Drone.DoesNotExist: 
            return Response({'message': 'Drone does not exist'}, status=status.HTTP_404_NOT_FOUND)
        


class DroneLoadMedicationView(APIView):
    """ Drone medication laods view class """

    serializer_class = DroneLoadMedicationSerialzer

    def get(self, request, serial_number):
        try:
            drone = Drone.objects.get(serial_number=serial_number)
            query_set = Medication.objects.filter(drone=drone)
            serializer = self.serializer_class(query_set, many=True)
            res = {
                'Medication': serializer.data,
                'message': 'Successfully fetched drone loaded medication'
            }
            return Response(res, status=status.HTTP_200_OK)

        except Drone.DoesNotExist: 
            return Response({'message': 'Drone does not exist'}, status=status.HTTP_404_NOT_FOUND)


class DroneBatteryLevelView(APIView):
    """ Drone battery level view class """

    serializer_class = DroneBatteryLevelSerializer

    def get(self, request, serial_number):

        try:
            drone = Drone.objects.get(serial_number=serial_number)
            serializer = self.serializer_class(drone)
            res = {
                'Battery Capacity': serializer.data,
                'message': 'Successfully fetched drone battery level'
            }
            return Response(res, status=status.HTTP_200_OK)

        except Drone.DoesNotExist: 
            return Response({'message': 'Drone does not exist'}, status=status.HTTP_404_NOT_FOUND)
