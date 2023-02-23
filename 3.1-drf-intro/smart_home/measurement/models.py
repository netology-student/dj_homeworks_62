from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=200, default="")

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(editable=False, auto_now=True)