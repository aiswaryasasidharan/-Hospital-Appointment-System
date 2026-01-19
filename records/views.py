from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

class AddRecordView(generics.CreateAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

class MyRecordsView(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicalRecord.objects.filter(patient=self.request.user)

