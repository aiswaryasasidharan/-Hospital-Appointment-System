from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, DoctorProfile, PatientProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','role','phone','gender','dob']

#register 

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data['role']
        user = User.objects.create_user(**validated_data)

        if role == 'doctor':
            DoctorProfile.objects.create(user=user)
        else:
            PatientProfile.objects.create(user=user)

        return user

 #Doctor Profile Serializer
class DoctorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested user info

    class Meta:
        model = DoctorProfile
        fields = ['id', 'user', 'specialization', 'experience', 'fees', 'available_days', 'available_from', 'available_to']

# Create or Update Doctor 
class DoctorCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = DoctorProfile
        fields = ['email', 'password', 'specialization', 'experience', 'fees', 'available_days', 'available_from', 'available_to']

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(email=email, password=password, role='doctor')
        doctor = DoctorProfile.objects.create(user=user, **validated_data)
        return doctor


# Patient Profile Serializer
class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PatientProfile
        fields = ['id', 'user', 'address', 'age']


# Create or Update Patient 

class PatientCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        write_only=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = PatientProfile
        fields = ['email', 'password', 'address', 'age']

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            email=email,
            password=password,
            role='patient'
        )

        patient = PatientProfile.objects.create(
            user=user,
            **validated_data
        )
        return patient
