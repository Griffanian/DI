import os, django,random,radar
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent.settings')
django.setup()

from polls.models import RentalRate,VehicleType,VehicleSize,Customer,Vehicle


if __name__ == '__main__':

    print("Populating database")
    fake = Faker()

    for i in range(50):
        id=random.randint(0,19)
        id2=random.randint(1,10)
        v=Vehicle(
            vehicle_type=VehicleType.objects.all()[id],
            date_created=radar.random_datetime(),
            real_cost=random.randint(500,10000),
            size=VehicleSize.objects.get(id=id2)
        )
        v.save()