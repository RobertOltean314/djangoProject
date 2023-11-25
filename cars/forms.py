from django import forms
from django.forms import TextInput, NumberInput, Textarea

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

        widgets = {
            'brand': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s brand '}),
            'model': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s model'}),
            'year': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s year'}),
            'color': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s color'}),
            'horse_power': NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s horse power'}),
            'technical_specifications': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the technical specifications'})
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

        widgets = {
            'brand': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s brand '}),
            'model': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s model'}),
            'year': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s year'}),
            'color': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s color'}),
            'horse_power': NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the car\'s horse power'})
        }
