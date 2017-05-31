#!/usr/bin/python
# -*- coding: utf-8 -*-


u"""Rysuje wyniki numerycznego rozwiązywania równań różniczkowych na podstawie
danych z pliku Wynik-numer_pliku.txt.

Plik z danymi ma mieć następującą postać.
1 linia = opis zawartości pliku.
2 linia = tytuł wykresu który zostanie utworzony.
3 linia = nazwa pliku z wykresem jaki zostać utworzony.
4 linia = linia zawiera opis danych z następnej linii, np. początek i koniec
przedziału całkowania numerycznego.
5 linia = zawiera dane opisane w linii wyżej.
6 linia = opis wyników numerycznych

Dalej są wyniki numeryczne w formacie
czas    dane numeryczne."""



######################################################################

import matplotlib.pyplot as plt

######################################################################


# Numer pliku z którego będą wczytywane dane.
numer_plik = 1
str_num_plik = str(numer_plik).zfill(2)


# Nazwa pliku który zostanie otworzony.
plik_nazwa = 'Wyniki-%s.txt' % str_num_plik


# Marginesy służą ,,poprawianiu'' wyglądu wykresu.
margines_1 = 0.2


t_list = []
x_list = []


with open(plik_nazwa) as plik:
    plik.readline()
    # Tytuł jaki zostanie nadany wykresowi.
    tytul_wykresu = plik.readline()
    # Nazwa pliku w którym zostanie utworzony rysunek.
    nazwa_rys_plik = plik.readline().strip()
    # Tworzy listę opisów parametrów opisu, dzięki której zostanie utworzona
    # dalsza część opisu. Opisy parametrów muszą być oddzielonym innym znakiem
    # niż spacja (bo we wzorach matematycznych jest ich dużo). W tym wypadku
    # jest to znak ,,\t''.
    param_opis_list = plik.readline().split('\t')
    # Lista parametrów rozwiązania numerycznego.
    param_wart_list = plik.readline().split()

    t_0, t_1 = float(param_wart_list[0]), float(param_wart_list[1])
    plik.readline()

    print param_opis_list
    print param_wart_list
    for i in xrange(len(param_opis_list)):
        tytul_wykresu += param_opis_list[i].strip() \
                         + " = " + param_wart_list[i].strip() + ", "

    tytul_wykresu += "\n"

    for linia in plik:
        dane_z_pliku = linia.split()
        t_list.append(float(dane_z_pliku[0]))
        x_list.append(float(dane_z_pliku[1]))



min_value = min(x_list) # Minimalna wartość wyników.
max_value = max(x_list) # Maksymalna wartość wyników.


fig = plt.figure()
fig.subplots_adjust(top = 0.8)
ax = fig.add_subplot(111)

ax.plot(t_list, x_list, color = 'r', label = 'numer')

ax.set_xlim(t_0 - margines_1, t_1 + margines_1)
ax.set_ylim(min_value - margines_1, max_value + margines_1)

ax.set_xlabel('t[s]')
ax.set_ylabel('x[m]')

ax.legend()
ax.set_title(tytul_wykresu)

fig.savefig(nazwa_rys_plik)
plt.show()
