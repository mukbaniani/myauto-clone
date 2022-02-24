from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("add-car-manufacturer", views.AddCarManufacturer, basename='add-car-manufacturer')
router.register("add-car-model", views.AddCarModel, basename='add-car-color')
router.register("add-car-color", views.AddCarColor, basename='add-car-color')
router.register("add-department", views.AddDepartment, basename="add-department")
router.register("add-employee", views.AddEmployee, basename="add-employee")

urlpatterns = router.urls

