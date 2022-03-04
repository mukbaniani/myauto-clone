from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractUser


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


class CustumUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, id_number, groups, department, password=None):
        if not email:
            raise ValueError(_('მეილის შეყვანა აუცილებელია'))
        if not first_name:
            raise ValueError(_('მომხმარებელი აუცილებელია'))
        if not groups:
            raise ValueError(_("ჯგუფის მითითება სავალდებულოა"))
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            id_number=id_number,
            department=department,
            groups=groups
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError(_('მეილის შეყვანა აუცილებელია'))
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Employee(AbstractUser):
    username = None
    first_name = models.CharField(max_length=25, verbose_name=_("სახელი"))
    last_name = models.CharField(max_length=25, verbose_name=_("გვარი"))
    email = models.EmailField(unique=True, verbose_name=_("მეილი"))
    phone = models.CharField(max_length=9, verbose_name=_("ტელეფონის ნომერი"),
                    validators=[RegexValidator(regex='^[0-9]{9}$', message='შეიყვანეთ მხოლოდ 9 ციფრი')], unique=True)
    id_number = models.CharField(max_length=11, verbose_name=_("პირადი ნომერი"),
                    validators=[RegexValidator(regex='^[0-9]{11}$', message='შეიყვანეთ 11 ციფრი')], unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("დეპარტამენტი"), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustumUserManager()


    def __str__(self):
        return f"{self.__class__.__name__}({self.first_name} -> {self.last_name})"


    class Meta:
        verbose_name = _("თანამშრომლები")


class CarTransmission(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('გადამცემთა კოლოფი'))

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

    
    class Meta:
        verbose_name = _('გადამცემთა კოლოფი')


class CarFuelType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('საწვავის ტიპი'))

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

    
    class Meta:
        verbose_name = _('საწვავის ტიპი')
