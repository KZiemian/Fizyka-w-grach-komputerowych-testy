#!/usr/bin/python
# -*- coding: utf-8 -*-


"""Rysuje """



######################################################################

import matplotlib.pyplot as plt

######################################################################



numer_pliku = 4
numer_rysunku = 11
string_num_pliku = str(numer_pliku).zfill(2)
string_num_rysunku = str(numer_rysunku).zfill(2)

plik_nazwa = 'Wynik-%s.txt' % string_num_pliku


margines_1 = 0.2

t_lista = []
y_lista = []
a_lista = [] # Rozwiązanie analityczne.
E_num_lista = [] 


with open(plik_nazwa) as plik:
    plik.readline().split()
    liczby_lista = plik.readline().split()
    t_0, t_1 = float(liczby_lista[0]), float(liczby_lista[1])
    plik.readline().split()
    for linia in plik:
        dane_z_pliku = linia.split()
        # print dane_z_pliku
        t_lista.append(float(dane_z_pliku[0]))
        y_lista.append(float(dane_z_pliku[1]))
        E_num_lista.append(float(dane_z_pliku[2]))
        a_lista.append(float(dane_z_pliku[3]))

fiugra = plt.fig()
plt.plot(t_lista, y_lista, color = 'r', label = 'numer')
plt.plot(t_lista, a_lista, color = 'g', label = 'anal')

plt.xlim(t_0 - margines_1, t_1 + margines_1)
# plt.ylim(-2.1, 2.1)
plt.legend()
plt.title('Algorytm Eulera')
plt.savefig('Rys-s1-%s.jpg' % string_num_rysunku)
plt.show()

