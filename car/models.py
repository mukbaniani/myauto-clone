from django.db import models
from base.models import CarManufacturer, CarColor, CarModel, CarTransmission, CarFuelType
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from . import consts
from PIL import Image


class CarPhoto(models.Model):
    photo = models.ImageField(verbose_name=_("ფოტო"), upload_to='images')

    def __str__(self):
        return f"{self.__class__.__name__}({self.photo})"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Car(models.Model):
    manufacturer = models.ForeignKey(
        CarManufacturer, on_delete=models.CASCADE, verbose_name=_('მწარმოებელი')
    )
    car_model = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, verbose_name=_('მოდელი')
    )
    car_color = models.ForeignKey(
        CarColor, on_delete=models.CASCADE, verbose_name=_('ფერი')
    )
    car_transmission = models.ForeignKey(
        CarTransmission, on_delete=models.CASCADE, verbose_name=_('გადამცემთა კოლოფი')
    )
    car_fuel_type = models.ForeignKey(
        CarFuelType, on_delete=models.CASCADE, verbose_name=_("საწვავის ტიპი")
    )
    photo = models.ForeignKey(
        CarPhoto, verbose_name=_("ფოტო"), on_delete=models.CASCADE
    )
    date_of_issue = models.CharField(choices=[(i, i) for i in range(1950, datetime.now().year, -1)], max_length=1, verbose_name=_("გამოშვების წელი"))
    steering_wheel_location = models.CharField(max_length=1, verbose_name=_("საჭის მდებარეობა"), choices=consts.Steering_Wheel_Location)
    engine_capacity = models.FloatField(verbose_name=_("ძრავის მოცულობა"))
    mileage = models.FloatField(verbose_name=_("გარბენი"))
    description = models.TextField(verbose_name=_("აღწერა"))
    price = models.FloatField(verbose_name=_("ფასი"))
    author_fullname = models.CharField(verbose_name=_("ავტორის სრული სახელი"), max_length=255)
    author_phone_number = models.CharField(max_length=9, verbose_name=_("ტელეფონის ნომერი"))

    def __str__(self):
        return f"{self.__class__.__name__}({self.manufacturer})"
