from django.shortcuts import render, redirect
from .models import Rental,Customer,Vehicle,VehicleType
from .forms import RentalForm,CustomerForm,VehicleForm
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
import random


def show_1_rental(request,pk):
    item = Rental.objects.get(id=pk)
    return render(request,'show_1_rental.html',{'item':item})

def show_all_rentals(request):
    unreturned=[item for item in Rental.objects.filter(return_date=None)]
    returned=[item for item in Rental.objects.exclude(return_date=None)]
    return render(request,'show_all_rental.html',{'unreturned':unreturned,'returned':returned})

@never_cache
def new_rental(request):
    if request.method == 'POST':
        form =  RentalForm(request.POST,initial={'return_date': ''})
        if form.is_valid():
            new_rent=form.save()
            new_id=new_rent.id
            return redirect(f'/rent/rental/{new_id}')
    else:
        form= RentalForm
    return render(request,'new.html',{'form':form})

def show_1_customer(request,pk):
    item=Customer.objects.get(id=pk)
    rentals=[item for item in Rental.objects.filter(customer__id=pk)]
    return render(request,'show_1_customer.html',{'item':item,'rentals':rentals})

def show_all_customers(request):
    customers=[item for item in Customer.objects.all().order_by('first_name')]
    return render(request,'show_all_customers.html',{'customers':customers})

@never_cache
def new_customer(request):
    if request.method == 'POST':
        form =  CustomerForm(request.POST)
        if form.is_valid():
            new_custom=form.save()
            new_id=new_custom.id
            return redirect(f'/rent/customer/{new_id}')
    else:
        form= CustomerForm
    return render(request,'new.html',{'form':form})

def show_1_vehicle(request,pk):
    item=Vehicle.objects.get(id=pk)
    return render(request,'show_1_vehicle.html',{'item':item})

def show_all_vehicles(request):
    rented={}
    unrented={}
    types=VehicleType.objects.all()
    for type in types:
        new_rented=[item for item in Vehicle.objects.filter(vehicle_type=type,rental__return_date__isnull=True)]
        rented.update({type.name:(new_rented)})
        new_unrented=[item for item in Vehicle.objects.filter(vehicle_type=type,rental__return_date__isnull=False)]
        unrented.update({type.name:(new_unrented)})
    return render(request,'show_all_vehicles.html',{'rented':rented.items(),'unrented':unrented.items()})

@never_cache
def new_vehicle(request):
    if request.method == 'POST':
        form =  VehicleForm(request.POST)
        if form.is_valid():
            new_vehic=form.save()
            new_id=new_vehic.id
            return redirect(f'/rent/Vehicle/{new_id}')
    else:
        form= VehicleForm
    return render(request,'new.html',{'form':form})
