from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import MedicationSerializer

class MedicationApiView(APIView):
    """ Medication Api View class"""

    serializer_class = MedicationSerializer

    def post(self, request):

        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {
                'medication': serializer.data,
                'message': 'Medication created successfully'
            }
            return Response(res, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': '{}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
