from rest_framework import serializers
from . import models
from django.utils.translation import gettext_lazy as _


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


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = models.Employee
        fields = ['first_name', 'last_name', 'email', 'id_number', 'phone', 
                'department', 'groups', 'is_superuser', 'is_staff', 'is_active', 'password1', 'password2', 'token']

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                raise serializers.ValidationError(_("პაროლი ერთმანეთს არ ემთხვევა"))
        else:
            raise serializers.ValidationError(_("პაროლის შეყვანა აუცილებელია"))
        return attrs
        

    def create(self, validated_data):
        password = validated_data.get("password1")
        employee = models.Employee(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            id_number=validated_data.get('id_number'),
            phone=validated_data.get('phone'),
            department=validated_data.get('department'),
            is_superuser=validated_data.get('is_superuser'),
            is_staff=validated_data.get('is_staff'),
            is_active=validated_data.get('is_active'),
        )
        employee.set_password(password)
        employee.save()
        return employee
