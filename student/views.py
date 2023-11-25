from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student


# CreateView: este o clasa dezvoltata de Django care va ajuta sa va definiti un obiect in
# baza de date si afisarea unui formular asociat modelului definit in models.py

# Principalele caractestici:

# Formular de Creare: automat se genereaza un formular asociat modelul pentru a adauga un obiect

# Procesarea datelor: gestionati procesarea datelor introduse in formular prin validare

# Redirectionare dupa creare: in momentul in care obiectul este creat cu success, utilizatorul poate fi
# redirectionat pe pagina dorita de noi.


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('home')
    permission_required = 'student.add_student'


# LISTVIEW: este o clasa dezvoltaa de Django care va ajuta pentru afisarea unei liste de obiecte dintr-un model in template

# Principale caracteristici:

# Gestionarea listei: automatizeaza procesul de preluare a listei de obiecte dintr-un model.
# Sablon/tEMPLATE implici: ListView foloseste un sablon implicit dar el va va lasa sa il folositi pe al vostru (model_list.html)


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_students'


# UpdateView este o clasa generica din Django  care este utilizata pentru a afisa un formular cu scopul de a actualiza
# informatiile despre obiectul existent din baza de date.

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')


# DeleteView este o clasa generica din Django care este utilizata pentru a sterge un obiect existent din baza de date

# O clasa generica este o clasa care este definnita cu parametri de tipuri variabile ce permit ca aceeasi clasa sa fie
# utilizata pentru diferite tipuri de date, oferind flexibilitae si reutilizare cod

# Beneficiile utilizarii claselor generice:

# 1. reducerea repetitiilor de cod
# 2. utilizarea principiilor DRY (Don't Repeat yourself)
# 2.1 Redundanta -> evitarea duplicarii de cod in diferite partie ale unei aplicatii. Daca exista un bloc de cod care este
# utilizat in mai multe locuri acesta trebuie refacut intr-o functie, metoda, clasa.
# 2.2 Refolosirea codului
# 2.3 Mentinerea coerentei si a coeziunii. -> Atunci cand o schimbare este necesara intr-o anumita functionalitate,
# aceasta trebuie facuta doar intr--un singur loc, asigurant coerenta si evitand discrepanta.


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')


# DetailView -> este o clasa generica in Django care este utilizata pentru a afisa detaliile unui singur obiect dintr-un
# model.

class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
