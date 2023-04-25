from django import forms
from .models import Category,Todo

class DateInput(forms.DateInput):
    input_type='date'

class TodoForm(forms.Form):
    title=forms.CharField(max_length=50)
    details=forms.CharField(max_length=200)
    deadline_date=forms.DateField(widget=DateInput)
    category=forms.ModelChoiceField(queryset=Category.objects.all())
    # class Meta:
    #     model = Todo
    #     exclude=['has_been_done']
    #     fields = '__all__'