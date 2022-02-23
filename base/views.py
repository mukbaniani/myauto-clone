from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer


class AddCarManufacturer(ModelViewSet):
    queryset = models.CarManufacturer.objects.all()
    serializer_class = serializer.CarManufacturerSerializer


class AddCarModel(ModelViewSet):
    queryset = models.CarModel.objects.all()
    serializer_class = serializer.CarModelSerializer


class AddCarColor(ModelViewSet):
    queryset = models.CarColor.objects.all()
    serializer_class = serializer.CarColorSerializer
