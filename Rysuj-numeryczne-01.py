#!/usr/bin/python
# -*- coding: utf-8 -*-


u"""Rysuje numeryczne rozwiązanie równań różniczkowych zwyczajnych
na podstawie danych z pliku plik_num_wyn.

Aby skrypt zadziałał plik_num_dane musi mieć następujący format.
1 linia = opis problemu którego wyniki dotyczą.
2 linia = pusta
3 linia = tytuł wykresu który zostanie utworzony prze matplotliba.
4 linia = pusta.
5 linia = nazwa pliku w którym zostanie zapisany wykres.
6 linia = pusta.
7 linia = zawiera opis parametrów rozwiązania, które znajdują się
w następnej linii. Dwa pierwsze są obowiązkowe, są to początek i koniec
przedziału całkowania numerycznego, pozostałe są opcjonalne.
Opis ma być w formacie LaTeXa, ty by dało się wygenerować ładne wzory
matematyczne w opisie.
8 linia = zawiera liczbowe wartość parametrów opisanych wyżej.
9 linia = pusta.
10 linia = opis tabel zawierających rezultat obliczeń numerycznych.

Dalej mają znajdować się wyniki obliczeń numerycznych w formacie
czas    położenie"""



######################################################################

import matplotlib.pyplot as plt

######################################################################


##############################
# Tworzenie nazwy pliku plik_num_wyn (plik_numeryczne_wyniki).
# W tym przypadku nazwy plików różnią się tylko numerem, więc najprościej
# zrobić to tak.

num_plik = 1 # num_plik = numer_pliku

plik_num_wyn = 'Wyniki-num-%s.txt' % str(num_plik).zfill(2)



# Marginesy służące poprawieniu wyglądu wykresu.
margines_1 = 0.2


##############################
# Pobieranie danych z pliku.

t_list = []
x_list = []


with open(plik_num_wyn) as plik:
    # Dużo lini w pliku jest pustych, aby je przejść po prostu je czytam.
    # Pewnie jest bardziej eleganckie rozwiązanie.
    plik.readline()
    plik.readline()
    # Tytuł jaki zostanie nadany wykresowi.
    tytul_wykresu = plik.readline()
    plik.readline()
    # Nazwa pliku w którym zostanie utworzony rysunek (nazwa_rysunku_plik).
    nazwa_rys_plik = plik.readline().strip()
    plik.readline()


    u"""Na podstawie wczytanych lini tworzy opis parametrów wyników
    numerycznych, który zostanie dołączony do tytul_wykresu i tym samym
    będą widoczne w tytule wykresu.

    Aby ten kod działa, poszczególne członu muszę być oddzielone 4 SPACJAMI.
    Wynika to z tego, że w kodzie LaTeXa jest dużo białych znaków,
    więc czysty split robija wyrażenia matematyczne."""
    # parametry_opis_lista
    param_opis_list = plik.readline().split("    ")
    # parametry_wartosci_lista
    param_wart_list = plik.readline().split()

    # Wczytuję początek i koniec przedziału całkowania numerycznego.
    t_0, t_1 = float(param_wart_list[0]), float(param_wart_list[1])
    plik.readline()

    # Pętla która dodaje nowe człony do tytulu_wykresu
    for i in xrange(len(param_opis_list)):
        tytul_wykresu += param_opis_list[i].strip() \
                         + " = " + param_wart_list[i].strip() + ", "

    # Po wykonaniu pętli, dodajemy znak pustej linii.
    tytul_wykresu += "\n"


    for linia in plik:
        dane_z_pliku = linia.split()
        t_list.append(float(dane_z_pliku[0]))
        x_list.append(float(dane_z_pliku[1]))


# Te zmienne wraz ze zmiennymi margines_* służą do poprawienia wyglądu
# wykresu.
min_value = min(x_list) # Minimalna wartość wyników.
max_value = max(x_list) # Maksymalna wartość wyników.



##############################
# Rysujemy wykres.

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
