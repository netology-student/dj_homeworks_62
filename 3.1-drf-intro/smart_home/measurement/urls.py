from django.urls import path
from .views import SensorList, UpdateSensor, AddMeasurements, SensorDetails

urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<pk>/', SensorDetails.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', AddMeasurements.as_view()),
]
