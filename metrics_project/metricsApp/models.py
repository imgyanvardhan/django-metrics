from django.db import models

# Create your models here.
class Metrics(models.Model):
    time = models.DateTimeField(primary_key=False)
    voltage = models.IntegerField(primary_key=False)
    current = models.IntegerField(primary_key=False)

    def __str__(self):
        return self.time + self.voltage + self.current