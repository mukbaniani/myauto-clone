from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("add-car-manufacturer", views.AddCarManufacturer, basename='add-car-manufacturer')
router.register("add-car-model", views.AddCarModel, basename='add-car-color')
router.register("add-car-color", views.AddCarColor, basename='add-car-color')
router.register("add-department", views.AddDepartment, basename="add-department")
router.register("add-employee", views.AddEmployee, basename="add-employee")
router.register("add-group", views.AddGroup, basename="add-group")
router.register("add-car-transmission", views.AddCarTransmission, basename="add-car-transmission")
router.register("add-car-fuel-type", views.AddCarFuelType, basename="add-car-fuel-type")

urlpatterns = router.urls

