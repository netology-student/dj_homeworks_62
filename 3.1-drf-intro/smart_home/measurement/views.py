# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.renderers import JSONRenderer

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework import generics

class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
class UpdateSensor(generics.UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
class AddMeasurements(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
class SensorDetails(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer