import os, django,random,radar
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent.settings')
django.setup()

from polls.models import RentalRate,Vehicle,VehicleSize,Rental,Customer
from datetime import datetime, timedelta
import random



if __name__ == '__main__':

    print("Populating database")
    fake = Faker()
    def random_after_date(start_date = datetime(1900, 1, 1)):
        end_date = datetime.now() - timedelta(days=1)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date

    for i in range(99):
        rental_date1=random_after_date()
        if i % 7 == 0:
           r=Rental(rental_date=rental_date1.strftime('%Y-%m-%d'),
            return_date=None,
            customer=Customer.objects.all()[i],
            vehicle=Vehicle.objects.all()[i])
        else:
            r=Rental(rental_date=rental_date1.strftime('%Y-%m-%d'),
            return_date=random_after_date(rental_date1),
            customer=Customer.objects.all()[i],
            vehicle=Vehicle.objects.all()[i])
        r.save()
        
