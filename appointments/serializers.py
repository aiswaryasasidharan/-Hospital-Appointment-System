from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'reason', 'status']
        read_only_fields = ['status']

    def create(self, validated_data):
        user = self.context['request'].user   # logged-in patient
        return Appointment.objects.create(
            patient=user,
            **validated_data
        )
