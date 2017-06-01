#!/usr/bin/python
# -*- coding: utf-8 -*-


# Popraw
u"""Rysuje na jednym wykresie numeryczne rozwiązanie równań różniczkowych
zwyczajnych z kilku plików, których nazwy są zawarte w liście plik_list
(pliki_lista) oraz rozwiązanie analityczne z pliku plik_anal.

Aby skrypt zadziałał pliki z nazw_plik_list musi mieć następujący format.
1 linia = opis problemu którego wyniki dotyczą.
2 linia = pusta
3 linia = tytuł wykresu który zostanie utworzony prze matplotliba.
4 linia = pusta.
5 linia = nazwa pliku w którym zostanie zapisany wykres.
6 linia = pusta.
7 linia = zawiera opis parametrów rozwiązania, które znajdują się
w następnej linii. Dwa pierwsze są obowiązkowe, są to początek i koniec
przedziału całkowania numerycznego, pozostałe są opcjonalne, ale muszą być
one jednakowe dla wszystkich plików. W programie jest spradzane, czy tak
rzeczywiście jest.

Opis ma być w formacie LaTeXa, ty by dało się wygenerować ładne wzory
matematyczne w tytule.
8 linia = zawiera liczbowe wartość parametrów opisanych wyżej.
9 linia = pusta.
10 linia = opis tabel zawierających rezultat obliczeń numerycznych.

Dalej mają znajdować się wyniki obliczeń numerycznych w formacie
czas    numeryczne (analityczne) rozwiazanie"""



######################################################################

import matplotlib.pyplot as plt

######################################################################



##############################
# Tworzenie nazwy listy plików pliki_list (pliki_lista). W tym przypadku
# nazwy poszczególnych plików z tej listy różnią się tylko numerem,
# więc najprościej zrobić to tak.


# Zakładając, że pliki noszą nazwę ,,Wyniki-num-x.txt'', gdzie ,,x''
# to numer pliku, poniższy kod generuje odpowiednią listę nazw plików.

# numery_plików_lista
num_plik_list = [1] # [1, 2, 3]

pliki_list = [] # (nazw_plików_lista)
for i in num_plik_list:
    pliki_list.append("Wyniki-%s.txt" % str(i).zfill(2))

    # Tu DOPISZ plik z rozwiązaniem analitycznym.


####################
# Zmienne pomocnicze do tworzenia rysunku

t_0 = 0.0 # Początkowa wartość na osi poziomej
t_1 = 0.0 # Końcowa wartość na osi poziomej

u"""Zmienne pomocnicze do ustawnienia skali rysunku. Na razie przypisujemy
im wartość 0.0, potem zaś będziemy je tylko zwiększa albo zmniejszać
komendą typu max_value = max(jakas_wartosc, max_value)."""
min_value = 0.0 # Minimalna wartość wyników
max_value = 0.0 # Maksymalna wartość wyników

# Marginesy służące poprawieniu wyglądu wykresu.
margines_1 = 0.2


# Kolory
# Na razie to kiepsko zrobione, ale na razie wystaczy
kolor_dlug_list = ['r', 'g', 'c', 'y'] # kolory_dluga_lista
kolor_list = kolor_dlug_list[:len(pliki_list)]
# Wycinam listę w taki sposób, żeby było po jednym kolorze na każdy plik.
# Chała, popraw.


##############################
# Tworzymy wykres


fig = plt.figure()
fig.subplots_adjust(top = 0.8)
ax = fig.add_subplot(111)

tytul_wykresu = ''
tytul_wykresu_tym = ''
u"""Wprowadzam te zmienne już teraz, aby móc sprawdzić, że dla wszystkich
plików tytuł jest taki sam."""


# Pętla tworzący wykres
for plik_elem in pliki_list: # plik_element
    t_list = []
    x_list = []

    with open(plik_elem) as plik:
        # Dużo lini w pliku jest pustych, aby je przejść po prostu je czytam.
        # Pewnie jest bardziej eleganckie rozwiązanie.
        plik.readline()
        plik.readline()
        # Tytuł jaki zostanie nadany wykresowi.
        if (tytul_wykresu == ''):
            tytul_wykresu = plik.readline()
        else:
            tytul_wykresu_tym = plik.readline()

        plik.readline()
        # Nazwa pliku w którym zostanie utworzony rysunek
        # (nazwa_rysunku_plik)
        nazwa_rys_plik = plik.readline().strip()
        plik.readline()

        u"""Na podstawie wczytanych lini tworzy opis parametrów wyników
        numerycznych, który zostanie dołączony do tytul_wykresu i tym samym
        będą widoczne w tytule wykresu.

        Aby ten kod działa, poszczególne członu muszę być oddzielone
        4 SPACJAMI. Wynika to z tego, że w kodzie LaTeXa jest dużo białych
        znaków, więc czysty split robija wyrażenia matematyczne."""
        # parametry_opis_lista
        param_opis_list = plik.readline().split("    ")
        # parametry_wartosci_lista
        param_wart_list = plik.readline().split()

        # Wczytuję początek i koniec przedziału całkowania numerycznego.
        # t_0_tymaczasowe, t_1_tymczasowe.
        t_0_tym, t_1_tym = float(param_wart_list[0]), \
                           float(param_wart_list[1])

        t_0 = min(t_0, t_0_tym)
        t_1 = max(t_1, t_1_tym)

        plik.readline()

        # Pętla która dodaje nowe człony do tytulu_wykresu
        if (tytul_wykresu == ''):
            for i in xrange(len(param_opis_list)):
                tytul_wykresu += param_opis_list[i].strip() \
                                 + " = " + param_wart_list[i].strip() + ", "

            # Po wykonaniu pętli, dodajemy znak pustej linii
            tytul_wykresu += "\n"
        elif (tytul_wykresu != ''):
            for i in xrange(len(param_opis_list)):
                tytul_wykresu_tym += param_opis_list[i].strip() \
                                     + " = " + param_wart_list[i].strip() \
                                     + ", "

            # Po wykonaniu pętli, dodajemy znak pustej linii
            tytul_wykresu += "\n"

        print "tytul wykresu = ", tytul_wykresu
        print "tytul wykresu_tym = ", tytul_wykresu_tym

        if (tytul_wykresu_tym != '') and (tytul_wykresu
                                          != tytul_wykresu_tym):
            print "Cos poszlo nie tak!\nTytuly wykresow w roznych plikach " \
                "nie sa jednakowe!"
            # Chała, popraw
            raise NameError


        # Pęlta zbierająca dane
        for linia in plik:
            dane_z_pliku = linia.split()
            t_list.append(float(dane_z_pliku[0]))
            x_list.append(float(dane_z_pliku[1]))

        min_value = min(min(x_list), min_value)
        max_value = max(max(x_list), max_value)

        ax.plot(t_lista, x_lista, color = 'r', label = label_plik)
        # Musisz wprowadzić label jako prametr w pliku. Zmienna label_plik nie
        # działa

ax.set_xlim(t_0 - margines_1, t_1 + margines_1)
ax.set_ylim(min_value - margines_1, max_value + margines_1)

ax.set_xlabel('t[s]')
ax.set_ylabel('x[m]')

ax.legend()
# print title_of_chart
ax.set_title(tytul_wykresu)

fig.savefig(nazwa_rys_plik)
plt.show()
