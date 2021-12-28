from django.urls import path

from .views import (
    MedicationApiView
)


urlpatterns = [
   path('create', MedicationApiView.as_view(), name='medication')
]