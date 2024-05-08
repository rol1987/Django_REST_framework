from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'changed_at']

class MeasurementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'changed_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

