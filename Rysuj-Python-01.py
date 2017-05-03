#!/usr/bin/python
# -*- coding: utf-8 -*-


"""Rysuje wyniki numerycznego rozwiązywania równań różniczkowych na podstawie
danych z pliku Wynik-numer_pliku.txt.

Pierwsza linia zawiera opis danych z następnej linii, np. początek i koniec
przedziału całkowania numerycznego.
Druga zawiera wyżej opisane dane.
W trzeciej puki co są śmieci.

W pliku tym dane mają być w formacie:
czas, dane numeryczne."""



######################################################################

import matplotlib.pyplot as plt

######################################################################



numer_pliku = 4
# Numer pliku z którego będą sczytywane dane
numer_rysunku = 12
# Numer rysunku który powstanie.

string_num_pliku = str(numer_pliku).zfill(2)
string_num_rysunku = str(numer_rysunku).zfill(2)


title_of_chart = "Algorytm Eulera"

plik_nazwa = 'Wynik-%s.txt' % string_num_pliku


margines_1 = 0.2

t_lista = []
y_lista = []


with open(plik_nazwa) as plik:
    plik.readline()
    liczby_lista = plik.readline().split()
    t_0, t_1 = float(liczby_lista[0]), float(liczby_lista[1])
    plik.readline()

    for linia in plik:
        dane_z_pliku = linia.split()
        t_lista.append(float(dane_z_pliku[0]))
        y_lista.append(float(dane_z_pliku[1]))

plt.plot(t_lista, y_lista, color = 'r', label = 'numer')

plt.xlim(t_0 - margines_1, t_1 + margines_1)
plt.ylim(min(y_lista) - margines_1, max(y_lista) + margines_1)

plt.legend()
plt.title(title_of_chart)

plt.savefig('Rys-%s.jpg' % string_num_pliku)
plt.show()

