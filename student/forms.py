from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # in formular se vor regasi toate fieldurile in ordinea definita in models.py

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data  # veti sctoca un dict cu valorile completate de utilizator in formular

        # Unicitate pe adresa de email
        get_email = cleaned_data['email']  # cleaned_data.get('email') ACCESAM VALOAREA INTRODUSA DE UTILIZATOR
        check_emails = Student.objects.filter(
            email=get_email)  # CAUTAM VALOAREA INTRODUSA DE UTILIZATOR IN TABELA PE COLOANA EMAIL
        if check_emails:  # DACA EXISTA CEL PUTIN UN STUDENT CU ACEEASI ADRESA DE EMAIL
            msg = 'Exista un student cu aceasta adresa de email'  # GENEREAM MESAJUL PENTRU AFISARE
            self._errors['email'] = self.error_class([msg])  # LOCALIZAM PE CEL FIELD VREM SA AFISAM MESAJUL ERORII

        # Validare pentru start_date si end_date. Daca start_date > end_date atunci sa ii afisam o eroare

        get_start_date = cleaned_data['start_date']
        get_end_date = cleaned_data['end_date']

        if get_start_date > get_end_date:
            msg = 'Start date este mai mare decat end date'
            self._errors['start_date'] = self.error_class([msg])

        # O unicitate pe first_name si last_name. Nu trebuie sa existe un alt student cu acelasi first_name si last_name

        get_first_name = cleaned_data['first_name']
        get_last_name = cleaned_data['last_name']
        check_students = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)
        if check_students:
            msg = 'Exista deja un student cu acelasi first name, respectiv lastname'
            self._errors['first_name'] = self.error_class([msg])

        # O validare pe description, sa nu poata adauga un text mai mare de 50 de caractere

        get_description = cleaned_data['description']
        if len(get_description) >= 50:
            msg = 'Dimensiunea textului este depasit. Maxim 50 de caractere'
            self._errors['description'] = self.error_class([msg])

        # O validare daca first_name < 3 si last_name < 3

        get_first_name = cleaned_data['first_name']
        get_last_name = cleaned_data['last_name']

        if len(get_first_name) < 3:
            msg = 'First name ul trebuie sa contina minim 3 caractere'
            self._errors['first_name'] = self.error_class([msg])

        if len(get_last_name) < 3:
            msg = 'Last name ul trebuie sa contina minim 3 caractere'
            self._errors['last_name'] = self.error_class([msg])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # in formular se vor regasi toate fieldurile in ordinea definita in models.py

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }
