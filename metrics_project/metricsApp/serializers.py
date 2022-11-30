from rest_framework import serializers
from metricsApp.models import Metrics
from django.db import models
import django_filters

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields=['time','voltage','current']