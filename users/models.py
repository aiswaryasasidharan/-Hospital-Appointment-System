from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager  

class User(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )

    username = None  # remove username 
    email = models.EmailField(unique=True)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # FIXED

    objects = UserManager()  # FIXED

    def __str__(self):
        return self.email


#doctor profile

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True, default=0)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    available_days = models.CharField(max_length=100, null=True, blank=True)
    available_from = models.TimeField(null=True, blank=True)
    available_to = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.user.email


#patient profile

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patients')
    address = models.CharField(max_length=255, null=True,blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.user.email

