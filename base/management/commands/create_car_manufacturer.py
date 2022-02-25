from django.core.management import BaseCommand
from ...models import CarManufacturer

class Command(BaseCommand):
    help = "create car manufacturer"

    def handle(self, *args, **options):
        manufacturer_list = [
            "BMW",
            "AUDI",
            "SUBARU",
            "JEEP"
        ]
        for department in manufacturer_list:
            CarManufacturer.objects.create(manufacturer=department)