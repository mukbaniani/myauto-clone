from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer
from rest_framework import response, status


class AddCarManufacturer(ModelViewSet):
    queryset = models.CarManufacturer.objects.all()
    serializer_class = serializer.CarManufacturerSerializer


class AddCarModel(ModelViewSet):
    queryset = models.CarModel.objects.all()
    serializer_class = serializer.CarModelSerializer


class AddCarColor(ModelViewSet):
    queryset = models.CarColor.objects.all()
    serializer_class = serializer.CarColorSerializer


class AddDepartment(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializer.DepartmentSerializer


class AddEmployee(ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer

    def list(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return response.Response({"result": "update employee data"}, status=status.HTTP_200_OK)
