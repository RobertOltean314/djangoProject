from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/', views.hello, name='first_func'),
    path('name/', views.show_name, name='name'),
]

# DEFINIREA UNUI PATH
# PREFIXUL VA FI UNIC
# NAME-UL VA FI UNIC


# path('first_page/', views.hello, name='first_func')
# path('specificati prefixul', mentionati ce def/class apelati, nume url pt identificare, pt HTML in special)

# path () este o functie utilizata pentru a defini rute (url-uri) pentru aplicatia web. Rutele specifica cum vor fi
# accesate diferite def/class in aplicatia web si ce actiuni trebuie sa se intample atunci cand un client web
# acceseaza o anumita cale (url).
