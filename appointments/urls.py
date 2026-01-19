from django.urls import path
from .views import (
    CreateAppointmentView,
    MyAppointmentsView,
    DoctorAppointmentsView,
    CancelAppointmentView,
    UpdateAppointmentStatusView
)

urlpatterns = [
    path("appointments/", CreateAppointmentView.as_view(), name="create-appointment"),
    path("appointments/my/", MyAppointmentsView.as_view(), name="my-appointments"),
    path("appointments/doctor/", DoctorAppointmentsView.as_view(), name="doctor-appointments"),
    path("appointments/<int:pk>/cancel/", CancelAppointmentView.as_view(), name="cancel-appointment"),
    path("appointments/<int:pk>/status/", UpdateAppointmentStatusView.as_view(), name="update-status"),
]


