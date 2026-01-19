from django.db import models
from users.models import User

class Appointment(models.Model):
    STATUS = (
        ('PENDING','PENDING'),
        ('ACCEPTED','ACCEPTED'),
        ('REJECTED','REJECTED'),
        ('CANCELLED','CANCELLED')
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')
    reason = models.TextField(null=True, blank=True)

