from django.core.management import BaseCommand
from ...models import CarModel, CarManufacturer


class Command(BaseCommand):
    help = 'create car model'

    def handle(self, *args, **options):
        models = [ 
            "m5", "forest", "test"
        ]
        
        for model in models:
            CarModel.objects.create(
                model=model,
                manufacturer=CarManufacturer.objects.order_by('?').first()
            )