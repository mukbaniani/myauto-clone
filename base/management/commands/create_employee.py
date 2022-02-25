from django.core.management import BaseCommand
from ...models import Employee, Department
from faker import Faker
from django.utils import timezone


class Command(BaseCommand):
    help = 'create employee'

    def handle(self, *args, **options):
        faker = Faker(["ka_GE"])
        timezone_now = timezone.now()
        for _ in range(10):
            em = Employee(
                first_name=faker.unique.first_name(),
                last_name=faker.unique.last_name(),
                id_number=faker.unique.pyint(
                    min_value=11111111111, max_value=99999999999
                ),
                phone=faker.unique.pyint(
                    min_value=111111111, max_value=999999999
                ),
                email=f"{faker.unique.first_name()}.{faker.unique.last_name()}.email.com",
                department=Department.objects.order_by("?").first(),
            )
            em.save()