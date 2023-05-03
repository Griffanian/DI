from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    image=forms.URLField()
    class Meta:
        model = UserProfile
        fields='__all__'
        widgets={
            'user':forms.HiddenInput()
        }