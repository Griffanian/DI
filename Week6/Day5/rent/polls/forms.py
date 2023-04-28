from django import forms
from .models import Customer,Vehicle, Rental 

class RentalForm(forms.ModelForm):
    vehicle=forms.ModelChoiceField(queryset=Vehicle.objects.filter(rental__return_date__isnull=False))
    class Meta:
        model = Rental
        exclude = ('return_date',)
        fields = ['rental_date','customer','vehicle']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'