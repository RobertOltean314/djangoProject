from django import forms
from django.forms import TextInput, EmailInput, Select

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Please enter your first name"}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the course you are teaching'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': Select(attrs={'class': 'form-select'})
        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': "Please enter your first name"}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the course you are teaching'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': Select(attrs={'class': 'form-select'})
        }
