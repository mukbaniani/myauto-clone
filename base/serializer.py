from rest_framework import serializers
from . import models


class CarManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarManufacturer
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModel
        fields = '__all__'


class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarColor
        fields = '__all__' 
