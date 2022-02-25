from django.core.management import BaseCommand
from ...models import CarColor


class Command(BaseCommand):
    help = 'create car color'

    def handle(self, *args, **options):
        color_list = [
            "ლურჯი",
            "წითელი",
            "მწვანე",
            "თეთრი"
        ]
        for department in color_list:
            CarColor.objects.create(color=department)
            