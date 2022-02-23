from django.db import models
from django.utils.translation import gettext_lazy as _


class CarManufacturer(models.Model):
    manufacturer = models.CharField(max_length=255, verbose_name=_('მწარმოებელი'))

    def __str__(self):
        return f"{self.__class__.__name__}({self.manufacturer})"


class CarModel(models.Model):
    model = models.CharField(max_length=255, verbose_name=_('მოდელი'))
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE, verbose_name=_('მწარმოებელი'))

    def __str__(self):
        return f"{self.__class__.__name__}({self.model}, {self.manufacturer})"


class CarColor(models.Model):
    color = models.CharField(max_length=90, verbose_name=_('ფერი'))

    def __str__(self):
        return f"{self.__class__.__name__}({self.color})"
