from django.contrib import admin
from .models import CarColor, CarManufacturer, CarModel


admin.site.register([CarModel, CarColor, CarManufacturer])
