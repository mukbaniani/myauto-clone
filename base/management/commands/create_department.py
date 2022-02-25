from django.core.management import BaseCommand
from ...models import Department

class Command(BaseCommand):
    help = "create department"

    def handle(self, *args, **options):
        department_list = [
            "ინფორმაციული ტექნოლოგიები",
            "გაყიდვები",
            "მარკეტინგი",
            "ფინანსები",
        ]
        for department in department_list:
            Department.objects.create(department_name=department)