from django import forms
from django.forms import TextInput, Select, NumberInput, Textarea

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the title'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the Author\'s name'}),
            'genre': Select(attrs={'class': 'form-select'}),
            'release_year': NumberInput(attrs={'class': 'form-select', 'placeholder': 'Please enter the release year'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the description of the book'})
        }


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the title'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the Author\'s name'}),
            'genre': Select(attrs={'class': 'form-select'}),
            'release_year': NumberInput(attrs={'class': 'form-select', 'placeholder': 'Please enter the release year'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the description of the book'})
        }
