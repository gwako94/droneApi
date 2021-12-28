from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Medication

class MedicationSerializer(serializers.ModelSerializer):
    """ Medication Serializer class """
    name = serializers.RegexField(
        regex='^[A-Za-z0-9\-\_]*$',
        required=True,
        validators=[UniqueValidator(
            queryset=Medication.objects.all(),
            message='The medication already exists.'
        )],
        error_messages={
            'invalid': 'medication name can only have letters, numbers, -, _.'
        }
    )

    code = serializers.RegexField(
        regex='^[A-Z0-9\_]*$',
        required=True,
                validators=[UniqueValidator(
            queryset=Medication.objects.all(),
            message='The medication already exists.'
        )],

    error_messages={
            'invalid': 'medication code can only have uppercase letters, numbers, _.'
        }

    )

    class Meta:
        model = Medication
        fields = '__all__'