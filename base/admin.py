from django.contrib import admin
from .models import CarColor, CarManufacturer, CarModel, Department, Employee


admin.site.register([CarModel, CarColor, CarManufacturer, Department, Employee])
