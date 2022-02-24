from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


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


class Department(models.Model):
    department_name = models.CharField(max_length=90, verbose_name=_("დეპარტამენტის სახელი"))


    def __str__(self):
        return f"{self.__class__.__name__}({self.department_name})"


class Employee(models.Model):
    first_name = models.CharField(max_length=25, verbose_name=_("სახელი"))
    last_name = models.CharField(max_length=25, verbose_name=_("გვარი"))
    email = models.EmailField(unique=True, verbose_name=_("მეილი"))
    phone = models.CharField(max_length=9, verbose_name=_("ტელეფონის ნომერი"),
                    validators=[RegexValidator(regex='^[0-9]{9}$', message='შეიყვანეთ მხოლოდ 9 ციფრი')], unique=True)
    id_number = models.CharField(max_length=11, verbose_name=_("პირადი ნომერი"),
                    validators=[RegexValidator(regex='^[0-9]{11}$', message='შეიყვანეთ 11 ციფრი')], unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("დეპარტამენტი"))


    def __str__(self):
        return f"{self.__class__.__name__}({self.first_name} -> {self.last_name})"
