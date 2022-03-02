from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer
from rest_framework import response, status, permissions
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin


class AddCarManufacturer(ModelViewSet, PermissionRequiredMixin):
    queryset = models.CarManufacturer.objects.all()
    serializer_class = serializer.CarManufacturerSerializer
    permission_required = ('base.add_carmanufacturer', 'base.change_carmanufacturer', 'base.view_carmanufacturer', 'base.delete_carmanufacturer')
    permission_classes = [permissions.DjangoModelPermissions]


class AddCarModel(ModelViewSet, PermissionRequiredMixin):
    queryset = models.CarModel.objects.all()
    serializer_class = serializer.CarModelSerializer
    permission_required = ('base.add_carmodel', 'base.change_carmodel', 'base.view_carmodel', 'base.delete_carmodel')
    permission_classes = [permissions.DjangoModelPermissions]


class AddCarColor(ModelViewSet, PermissionRequiredMixin):
    queryset = models.CarColor.objects.all()
    serializer_class = serializer.CarColorSerializer
    permission_required = ('base.add_carcolor', 'base.change_carcolor', 'base.view_carcolor', 'base.delete_carcolor')
    permission_classes = [permissions.DjangoModelPermissions]


class AddDepartment(ModelViewSet, PermissionRequiredMixin):
    queryset = models.Department.objects.all()
    serializer_class = serializer.DepartmentSerializer
    permission_required = ('base.add_department', 'base.change_department', 'base.view_department', 'base.delete_department')
    permission_classes = [permissions.DjangoModelPermissions]


class AddEmployee(ModelViewSet, PermissionRequiredMixin):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    permission_required = ('base.add_employee', 'base.change_employee', 'base.view_employee', 'base.delete_employee')
    permission_classes = [permissions.DjangoModelPermissions]

    def list(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return response.Response({"result": "update employee data"}, status=status.HTTP_200_OK)


class AddGroup(ModelViewSet, PermissionRequiredMixin):
    queryset = Group.objects.all()
    serializer_class = serializer.GroupSerializer
    permission_required = ('base.add_group', 'base.change_group', 'base.view_group', 'base.delete_group')
    permission_classes = [permissions.DjangoModelPermissions]

    def list(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)
