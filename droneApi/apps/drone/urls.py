from django.urls import path

from .views import (
    DroneApiView
)


urlpatterns = [
   path('register', DroneApiView.as_view(), name='drones')
]