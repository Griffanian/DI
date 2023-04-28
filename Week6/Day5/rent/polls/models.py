from django.db import models

class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50,default='')
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):

    vehicle_type = models.ForeignKey('VehicleType',on_delete=models.CASCADE)
    date_created = models.DateField()
    real_cost = models.FloatField()
    size = models.ForeignKey('VehicleSize',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.size.name} {self.vehicle_type} #{self.id}'

class VehicleType(models.Model):

    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class VehicleSize(models.Model):

    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class Rental(models.Model):

    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"rental #{self.id}"
    
class RentalRate(models.Model):

    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType,on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize,on_delete=models.CASCADE)


