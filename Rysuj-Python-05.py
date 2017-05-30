#!/usr/bin/python
# -*- coding: utf-8 -*-


# Ten plik ma rysować również energię, tylko trzeba ten kod napisać.
u"""Rysuje wyniki numerycznego rozwiązywania oraz energię dla tego rówanania
różniczkowego na podstawie danych z pliku w liście lista_plikow.
DOKONCZ

Plik z danymi ma mieć następującą postać.
Pierwsza zawiera (jakiś) opis danych, który posłuży za tytuł rysunku.
Druga linia zawiera opis danych z następnej linii, np. początek i koniec
przedziału całkowania numerycznego.
Trzecia zawiera wyżej opisane dane.
W czwartej jest opis danych numerycznych.

Dalej są dane w formacie
czas    dane numeryczne."""



######################################################################

import matplotlib.pyplot as plt

######################################################################



# Zakładając, że pliki noszą nazwę ,,Wyniki-x.txt'', gdzie ,,x'' to numer
# pliku, poniższy kod generuje odpowiednią listę nazw plików.
lista_numerow_plikow = [10, 11, 12]

lista_plikow = []
for i in lista_numerow_plikow:
    lista_plikow.append("Wyniki-%s.txt" % str(i).zfill(2))


# Aby każdy wykres miał inny kolor wprowadzam listę kolorów
lista_kolorow = ['g', 'y', 'c']

# Numer rysunku który powstanie.
numer_rysunku = 2

string_num_rysunku = str(numer_rysunku).zfill(2)

# Zmienne pomocnicze do rysunku
min_value = 0.0
max_value = 0.0

t_0 = 0.0
t_1 = 0.0


margines_1 = 0.2


fig = plt.figure()
fig.subplots_adjust(top = 0.8)
ax = fig.add_subplot(111)


 # Zmienna do zliczania obiegów, powinna się przydać
num_petli = 0


for plik_nazwa in lista_plikow:

    t_lista = []
    x_lista = []

    with open(plik_nazwa) as plik:
        plik.readline()
        plik.readline()
        title_of_chart = plik.readline()
        rysunek_nazwa = plik.readline().strip()
        nazwy_liczb = plik.readline().split("    ")
        # Zakładam, że nazwy tych liczb są oddzielone 4 spacjami,
        # a nie po prostu białymi znakami.
        liczby_lista = plik.readline().split()
        opis_wykresu = str(nazwy_liczb[-1].strip()) \
                       + " = " + liczby_lista[-1].strip()

        for i in xrange(len(nazwy_liczb) - 1):
            title_of_chart += nazwy_liczb[i].strip() \
                              + " = " + liczby_lista[i].strip() + ", "

        # Ta linie musi być na poziomie poprzedniego fora.
        title_of_chart += "\n"

        t_0_temp, t_1_temp = float(liczby_lista[0]), float(liczby_lista[1])
        plik.readline()

        t_0 = min(t_0, t_0_temp)
        t_1 = max(t_1, t_1_temp)

        for linia in plik:
            dane_z_pliku = linia.split()
            # print dane_z_pliku
            t_lista.append(float(dane_z_pliku[0]))
            x_lista.append(float(dane_z_pliku[1]))


    min_value = min(min(x_lista), min_value)
    max_value = max(max(x_lista), max_value)

    ax.plot(t_lista, x_lista, color = lista_kolorow[num_petli],
            label = opis_wykresu)

    num_petli += 1


ax.set_xlim(t_0 - margines_1, t_1 + margines_1)
ax.set_ylim(min_value - margines_1, max_value + margines_1)

ax.set_xlabel('t[s]')
ax.set_ylabel('x[m]')

ax.legend()
# print title_of_chart
ax.set_title(title_of_chart)

fig.savefig(rysunek_nazwa)
plt.show()

