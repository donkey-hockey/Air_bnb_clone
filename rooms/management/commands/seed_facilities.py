from rooms.models import Facility
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command make Facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for a in facilities:
            Facility.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Facilities created"))
