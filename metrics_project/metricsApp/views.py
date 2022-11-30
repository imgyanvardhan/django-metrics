from django.shortcuts import render
from metricsApp.models import Metrics
from metricsApp.serializers import MetricsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class MetricsFilter(django_filters.FilterSet):
    #date_range = django_filters.NumberFilter(field_name='time', lookup_expr='time')
    start = django_filters.DateTimeFilter(field_name='time', lookup_expr='gte')
    end = django_filters.DateTimeFilter(field_name='time', lookup_expr='lte')
    class Meta:
        model = Metrics
        fields = ['start','end']

'''
@api_view(['GET'])
def find_metrics(request):
    date_range = Metrics.objects.filter(time = request.data['time'])
    serializer = MetricsSerializer(date_range,many=True)
    return Response(serializer.data)
'''

class MetricsViewSet(viewsets.ModelViewSet):
    queryset=Metrics.objects.all()
    serializer_class = MetricsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MetricsFilter

