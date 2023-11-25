from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

@login_required()
def hello(request):
    return HttpResponse('Hello World!')

@login_required()
def show_name(request):
    return HttpResponse('Hello, Mariana!')


# am definit o functie hello care returneaza un string -> Hello World

