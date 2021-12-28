from django.urls import path

from .views import (
    DroneApiView,
    DroneBatteryLevelView,
    DroneLoadMedicationView,
    DroneLoadingView
)


urlpatterns = [
   path('register', DroneApiView.as_view(), name='drones'),
   path('loading/<serial_number>', DroneLoadingView.as_view(), name='drone_loading'),
   path('loads/<serial_number>', DroneLoadMedicationView.as_view(), name='drone_loads'),
   path('available', DroneApiView.as_view(), name='drone_available'),
   path('battery_level/<serial_number>', DroneBatteryLevelView.as_view(), name='drone_battery_level'),
]
