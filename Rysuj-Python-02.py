#!/usr/bin/python
# -*- coding: utf-8 -*-



u"""Rysuje wyniki numerycznego rozwiązywania równań różniczkowych na podstawie
danych z pliku Wynik-numer_pliku.txt.

Plik z danymi ma mieć następującą postać.
Pierwsza zawiera (jakiś) opis danych, który posłuży za tytuł rysunku.
Druga linia zawiera opis danych z następnej linii, np. początek i koniec
przedziału całkowania numerycznego.
Trzecia zawiera wyżej opisane dane.
W czwartej jest opis danych numerycznych.

Dalej są dane w formacie
czas    dane numeryczne    dane analityczne."""



######################################################################

import matplotlib.pyplot as plt

######################################################################



numer_pliku = 1
# Numer pliku z którego będą sczytywane dane
numer_rysunku = 1
# Numer rysunku który powstanie.

string_num_pliku = str(numer_pliku).zfill(2)
string_num_rysunku = str(numer_rysunku).zfill(2)

plik_nazwa = 'Wynik-%s.txt' % string_num_pliku

margines_1 = 0.2


t_lista = []
x_lista = []
a_lista = [] # Rozwiązanie analityczne.


with open(plik_nazwa) as plik:
    title_of_chart = plik.readline().strip()
    rysunek_nazwa = plik.readline().strip()
    plik.readline()
    liczby_lista = plik.readline().split()
    t_0, t_1 = float(liczby_lista[0]), float(liczby_lista[1])
    plik.readline()

    for linia in plik:
        dane_z_pliku = linia.split()
        # print dane_z_pliku
        t_lista.append(float(dane_z_pliku[0]))
        x_lista.append(float(dane_z_pliku[1]))
        a_lista.append(float(dane_z_pliku[2]))



min_value = min(min(x_lista), min(a_lista))
max_value = max(max(x_lista), max(a_lista))

plt.plot(t_lista, x_lista, color = 'r', label = 'numer')
plt.plot(t_lista, a_lista, color = 'g', label = 'anal')

plt.xlim(t_0 - margines_1, t_1 + margines_1)
plt.ylim(min_value - margines_1, max_value + margines_1)

plt.xlabel('t[s]')
plt.ylabel('x[m]')

plt.legend()
plt.title(title_of_chart)

plt.savefig(rysunek_nazwa)
plt.show()

