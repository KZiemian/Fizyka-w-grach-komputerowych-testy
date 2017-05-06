#!/usr/bin/python
# -*- coding: utf-8 -*-



u"""Rysuje wyniki numerycznego rozwiązywania równań różniczkowych na podstawie
danych z pliku Wynik-numer_pliku.txt.

Plik z danymi ma mieć następującą postać.
Pierwsza zawiera (jakiś) opis danych, który posłuży za tytuł rysunku.
Druga zawiera nazwę rysunku jaki ma powstać.
Trzecia linia zawiera opis danych z następnej linii, np. początek i koniec
przedziału całkowania numerycznego.
Czwarta zawiera wyżej opisane dane.
W piątej jest opis danych numerycznych.

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
    title_of_chart = plik.readline()
    rysunek_nazwa = plik.readline().strip()
    nazwy_liczb = plik.readline().split()
    liczby_lista = plik.readline().split()

    for i in xrange(len(nazwy_liczb)):
        title_of_chart += nazwy_liczb[i].strip() \
                          + " = " + liczby_lista[i].strip() + ", "

    title_of_chart += "\n"

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


fig = plt.figure()
fig.subplots_adjust(top = 0.8)
ax = fig.add_subplot(111)

ax.plot(t_lista, x_lista, color = 'r', label = 'numer')
ax.plot(t_lista, a_lista, color = 'g', label = 'anal')

ax.set_xlim(t_0 - margines_1, t_1 + margines_1)
ax.set_ylim(min_value - margines_1, max_value + margines_1)

ax.set_xlabel('t[s]')
ax.set_ylabel('x[m]')

ax.legend()
# print title_of_chart
ax.set_title(title_of_chart)

fig.savefig(rysunek_nazwa)
plt.show()

