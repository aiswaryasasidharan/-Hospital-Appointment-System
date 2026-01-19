from rest_framework import generics,viewsets,permissions
from .models import DoctorProfile, PatientProfile
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer,DoctorProfileSerializer, DoctorCreateSerializer, PatientProfileSerializer,PatientCreateSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Admin can CRUD doctors

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DoctorCreateSerializer
        return DoctorProfileSerializer

    permission_classes = [IsAuthenticated]


# Admin can CRUD patients
class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PatientCreateSerializer
        return PatientProfileSerializer

    permission_classes = [IsAuthenticated]