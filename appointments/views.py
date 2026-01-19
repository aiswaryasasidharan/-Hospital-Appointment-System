from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer


# Patient creates appointment
class CreateAppointmentView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


# Patient views only their own appointments
class MyAppointmentsView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != "patient":
            raise PermissionDenied("Only patients can view this.")
        return Appointment.objects.filter(patient=self.request.user)


# Doctor views their assigned appointments
class DoctorAppointmentsView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != "doctor":
            raise PermissionDenied("Only doctors can view this.")
        return Appointment.objects.filter(doctor=self.request.user)


# Patient cancels appointment
class CancelAppointmentView(generics.UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()

    def update(self, request, *args, **kwargs):
        appt = self.get_object()
        if appt.patient != request.user:
            raise PermissionDenied("Not your appointment.")
        appt.status = "cancelled"
        appt.save()
        return Response(AppointmentSerializer(appt).data)


# Doctor updates status
class UpdateAppointmentStatusView(generics.UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()

    def update(self, request, *args, **kwargs):
        appt = self.get_object()
        if appt.doctor != request.user:
            raise PermissionDenied("Not your appointment.")
        status_value = request.data.get("status")
        if not status_value:
            raise ValidationError({"status": "Required"})
        appt.status = status_value
        appt.save()
        return Response(AppointmentSerializer(appt).data)

