from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateView: este o clasa dezvoltata de Django folosita pentru a afisa un sablon(o pagina html)

# Principalele caracteristici sunt:

# Manipularea Sabloanelor: este proiectat pentru a lucra cu pagini html. Puteti sa specificati tempalte-ul
# pe care doriti sa il utilizati pentru a afisa continutul paginii

# Gestionarea Contextului: Puteti sa furnizati context suplimentare pentru template, permitand astefel
# trimiterea de variabile si informatii catre template pentru a fi afisate


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html' # mentionatm fisierul html pe care il dorim afisat in interfata