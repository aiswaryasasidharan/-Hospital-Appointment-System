from django.db import models
from users.models import User
from appointments.models import Appointment

class MedicalRecord(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rec_doctor")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rec_patient")
    diagnosis = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

