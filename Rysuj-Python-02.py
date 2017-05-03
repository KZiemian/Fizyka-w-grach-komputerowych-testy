#!/usr/bin/python
# -*- coding: utf-8 -*-



"""Rysuje rozwiązanie numeryczne i analityczne na podstawie danych z pliku
Wynik-numer_pliku.txt. W pliku tym dane mają być w formacie.
W pierwszej linii
czas, numeryczne, analityczne."""



######################################################################

import matplotlib.pyplot as plt

######################################################################



numer_pliku = 4
numer_rysunku = 11
string_num_pliku = str(numer_pliku).zfill(2)
string_num_rysunku = str(numer_rysunku).zfill(2)

title_of_chart = "Algorytm Eulera"

plik_nazwa = 'Wynik-%s.txt' % string_num_pliku


margines_1 = 0.2

t_lista = []
y_lista = []
a_lista = [] # Rozwiązanie analityczne.


with open(plik_nazwa) as plik:
    plik.readline()
    liczby_lista = plik.readline().split()
    t_0, t_1 = float(liczby_lista[0]), float(liczby_lista[1])
    plik.readline()

    for linia in plik:
        dane_z_pliku = linia.split()
        # print dane_z_pliku
        t_lista.append(float(dane_z_pliku[0]))
        y_lista.append(float(dane_z_pliku[1]))
        a_lista.append(float(dane_z_pliku[2]))

min_value = min(min(y_lista), min(a_lista))
max_value = max(max(y_lista), max(a_lista))

plt.plot(t_lista, y_lista, color = 'r', label = 'numer')
plt.plot(t_lista, a_lista, color = 'g', label = 'anal')
plt.xlim(t_0 - margines_1, t_1 + margines_1)
plt.ylim(min_value - margines_1, max_value + margines_1)
plt.legend()
plt.title(title_of_chart)
plt.savefig('Rys-s01-%s.jpg' % string_num_rysunku)
plt.show()

