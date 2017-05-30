#!/usr/bin/python
# -*- coding: utf-8 -*-


# Ale chała popraw.
# Ten plik ma rysować również energię, tylko trzeba ten kod napisać.
u"""Rysuje wyniki numerycznego rozwiązywania oraz energię dla tego rówanania
różniczkowego na podstawie danych z pliku w liście lista_plikow.
DOKONCZ
Ten program robi jeszcze wykresy energii.

Plik z danymi ma mieć następującą postać.
Pierwsza zawiera (jakiś) opis danych, który posłuży za tytuł rysunku.
Druga linia zawiera opis danych z następnej linii, np. początek i koniec
przedziału całkowania numerycznego.
Trzecia zawiera wyżej opisane dane.
W czwartej jest opis danych numerycznych.

Dalej są dane w formacie
czas    dane numeryczne    energia."""



######################################################################

import matplotlib.pyplot as plt

######################################################################



# Zakładając, że pliki noszą nazwę ,,Wyniki-x.txt'', gdzie ,,x'' to numer
# pliku, poniższy kod generuje odpowiednią listę nazw plików.
lista_numerow_plikow = [1, 2, 3]

lista_plikow = []
for i in lista_numerow_plikow:
    lista_plikow.append("Wyniki-num-%s.txt" % str(i).zfill(2))

# Aby każdy wykres miał inny kolor wprowadzam listę kolorów
lista_kolorow = ['g', 'y', 'c']

# Numer rysunku który powstanie.
numer_rysunku = 6

string_num_rysunku = str(numer_rysunku).zfill(2)

# Wartość przedziału początkowego i końcowego dobieram w kodzie, teraz
# nadej im wartość 0.
t_0 = 0.0
t_1 = 0.0

# Zmienne pomocnicze
# Mało elegancie zmień to
ener_anal = 3.51709

# Zmienne pomocnicze do rysunku
min_val_x = 0.0
max_val_x = 0.0

min_val_ener = 0.0
max_val_ener = 0.0

margines_1 = 0.2



# Tworzymy rysunek.
fig = plt.figure()
fig.subplots_adjust(top = 0.8)
ax_1 = fig.add_subplot(121)
ax_2 = fig.add_subplot(122)


 # Zmienna do zliczania obiegów, powinna się przydać
num_petli = 0


for plik_nazwa in lista_plikow:

    t_lista = []
    x_lista = []
    ener_lista = []

    with open(plik_nazwa) as plik:
        plik.readline()
        plik.readline()
        tytul_wykresu = plik.readline()
        nazwa_rys_plik = plik.readline().strip()
        nazwy_liczb = plik.readline().split("\t")
        # Zakładam, że nazwy tych liczb są oddzielone \t,
        # a nie po prostu białymi znakami.
        liczby_lista = plik.readline().split()
        # opis_wykresu = str(nazwy_liczb[-1].strip()) \
            #                + " = " + liczby_lista[-1].strip()

        # for i in xrange(len(nazwy_liczb) - 1):
        #     tytul_wykresu += nazwy_liczb[i].strip() \
            #                       + " = " + liczby_lista[i].strip() + ", "

        # # Ta linie musi być na poziomie poprzedniego fora.
        # tytul_wykresu += "\n"

        t_0_temp, t_1_temp = float(liczby_lista[0]), float(liczby_lista[1])
        plik.readline()

        t_0 = min(t_0, t_0_temp)
        t_1 = max(t_1, t_1_temp)

        for linia in plik:
            dane_z_pliku = linia.split()
            # print dane_z_pliku
            t_lista.append(float(dane_z_pliku[0]))
            x_lista.append(float(dane_z_pliku[1]))
            ener_lista.append(float(dane_z_pliku[2]))


    min_val_x = min(min(x_lista), min_val_x)
    max_val_x = max(max(x_lista), max_val_x)
    min_val_ener = min(min(ener_lista), min_val_ener)
    max_val_ener = max(max(ener_lista), max_val_ener)

    ax_1.plot(t_lista, x_lista, color = lista_kolorow[num_petli],
              label = opis_wykresu)
    ax_2.plot(t_lista, ener_lista, color = lista_kolorow[num_petli],
              label = opis_wykresu)

    num_petli += 1


ener_li_anal = []
t_lista = []

t = 0.0

while (t <= 15.0):
    # Mało eleganckie, popraw
    t_lista.append(t)
    ener_li_anal.append(ener_anal)
    t += 0.001

ax_2.plot(t_lista, ener_li_anal, color = "r", label = "anal")

ax_1.set_xlim(t_0 - margines_1, t_1 + margines_1)
ax_1.set_ylim(min_val_x - margines_1, max_val_x + margines_1)

ax_2.set_xlim(t_0 - margines_1, t_1 + margines_1)
ax_2.set_ylim(min_val_ener - margines_1, max_val_ener + margines_1)

ax_1.set_xlabel('t[s]')
ax_1.set_ylabel('x[m]')

ax_2.set_xlabel('t[s]')
ax_2.set_ylabel('E[J]')

ax_1.legend()
ax_2.legend()
# print tytul_wykresu
ax_1.set_title(tytul_wykresu)

fig.savefig(nazwa_rys_plik)
plt.show()
