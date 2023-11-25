from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select, widgets, CheckboxInput

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email address'}),
            'trainer': Select(attrs={'class': 'form-select'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': "Please enter your message", 'rows': 5}),

        }