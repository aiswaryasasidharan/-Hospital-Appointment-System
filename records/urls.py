from django.urls import path
from .views import AddRecordView, MyRecordsView

urlpatterns = [
    path('add/', AddRecordView.as_view()),
    path('my/', MyRecordsView.as_view()),
]
