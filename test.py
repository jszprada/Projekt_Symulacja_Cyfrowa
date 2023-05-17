from gaussa import random_gaussian

from row import random_uniform
from wyk import random_exponential
import numpy as np
import math

seed_B1 =44
seed_B2 =22
seed_wyk =134
seed_row =312
np.random.seed(seed_B1)
gauss_B1=[]
i=0
while i<100000:
    gauss_B1.append(random_gaussian())
    i+=1

np.random.seed(seed_B2)
gauss_B2=[]
i=0
while i<100000:
    gauss_B2.append(random_gaussian())
    i+=1

np.random.seed(seed_wyk)
wyk=[]
i=0
while i<100000:
    wyk.append(random_exponential())
    i+=1

np.random.seed(seed_row)
row=[]
i=0
while i<100000:
    row.append(random_uniform())
    i+=1

def oblicz_Pb_B1(d):
    s=gauss_B1.pop()
    return 4.56 - 22 * math.log10(d) + s
def oblicz_Pb_B2(d):
    s=gauss_B2.pop()
    return 4.56 - 22 * math.log10(d) + s
def przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny):
    pierwsza_osoba = kolejka2.kolejka2.pop(0)
    pierwsza_osoba.czas = czas_ogolny + 20
    kolejka.dodaj_osobe(pierwsza_osoba)
    print("Osoba przeniesiona z kolejki 2 do kolejki 1")
class Osoba:
    licznik_osob = 0
    licznik_przelaczen = 0
    #stacja_bazowa = 1
    def __init__(self, czas,stacja_bazowa = 1):
        global ID
        self.id = ID
        self.czas = czas
        self.droga = 2000
        self.stacja_bazowa=stacja_bazowa
        Osoba.licznik_osob += 1
    @staticmethod
    def pobierz_licznik():
        return Osoba.licznik_osob
    @staticmethod
    def pobierz_licznik_przelaczen():
        return Osoba.licznik_przelaczen
    def zmien_stacje_bazowa_na_B2(self):
        if self.stacja_bazowa == 1:
            self.stacja_bazowa = 2
            Osoba.licznik_przelaczen += 1
        else:
            pass
    def zmien_stacje_bazowa_na_B1(self):
        if self.stacja_bazowa == 2:
            self.stacja_bazowa = 1
            Osoba.licznik_przelaczen += 1
        else:
            pass
    def wypisz_dane(self):
        print(f"Id: {self.id}, czas: {self.czas}, droga: {self.droga},stacja_bazowa: {self.stacja_bazowa}")

class Kolejka:
    def __init__(self):
        self.kolejka = []
        self.max_rozmiar = 20
        self.id = 0

    def dodaj_osobe(self, osoba):
        if len(self.kolejka) < self.max_rozmiar:
            self.id += 1
            osoba.id = self.id
            self.kolejka.append(osoba)
        else:
            pass
    def usun_osobe(self, osoba):
        self.kolejka.remove(osoba)

    def wypisz_kolejke(self):
        for osoba in self.kolejka:
            osoba.wypisz_dane()
class Kolejka2:
    def __init__(self):
        self.kolejka2 = []
        self.max_rozmiar = float("inf")
        self.id = 0
    def dodaj_osobe(self, osoba):
            self.id += 1
            osoba.id = self.id
            self.kolejka2.append(osoba)
    def wypisz_kolejke(self):
        for osoba in self.kolejka2:
            osoba.wypisz_dane()

B2_location=5000
czas_ogolny = 0
czas_systemu = 0

kolejka = Kolejka()
kolejka2=Kolejka2()
ID = 1
do_update = True

czas_z=czas_ogolny+20
osoba=Osoba(czas_z)
kolejka.dodaj_osobe(osoba)
print(f"Osoba {osoba.id} dodana do kolejki. Czas:", czas_z)

czas_ogolny +=wyk.pop()#5
while True:
    najmniejszy_czas = min(kolejka.kolejka, key=lambda x: x.czas)# or czas_ogolny
    if czas_ogolny == najmniejszy_czas.czas:
        do_update = False

    czas_systemu = min(najmniejszy_czas.czas, czas_ogolny)
    print("Czas ogolny:", czas_ogolny)
    print("Czas min obiektow:", najmniejszy_czas.czas)
    print("Czas systemu:", czas_systemu)

    if czas_systemu == najmniejszy_czas.czas:
        najmniejszy_czas.droga +=  0.02*row.pop()#50
        najmniejszy_czas.wypisz_dane()
        najmniejszy_czas.czas += 20
        if najmniejszy_czas.droga >= 3000:
            kolejka.usun_osobe(najmniejszy_czas)
            if len(kolejka2.kolejka2) > 0:
                przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny)
            print(f"Osoba {najmniejszy_czas.id, najmniejszy_czas.czas, najmniejszy_czas.droga} dotarła do celu")
        else:
            print("Czas po zmianie:", najmniejszy_czas.czas)
            pass
        Pb_B1 = oblicz_Pb_B1(najmniejszy_czas.droga)
        Pb_B2 = oblicz_Pb_B2(B2_location - najmniejszy_czas.droga)
        if Pb_B2 - Pb_B1 > 20:# dopracować?
            kolejka.usun_osobe(najmniejszy_czas)
            print(f"Osoba {najmniejszy_czas.id} straciła połączenie")
            if len(kolejka2.kolejka2) > 0:
                przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny)
        elif Pb_B2>Pb_B1 and Pb_B2 - Pb_B1 >= 3:# dopracować?
            najmniejszy_czas.zmien_stacje_bazowa_na_B2()
            print(f"Osoba {najmniejszy_czas.id} zmieniła stację bazową na {najmniejszy_czas.stacja_bazowa}, moc z B1 {Pb_B1} a z B2 {Pb_B2}")
        elif Pb_B1>Pb_B2 and Pb_B1 - Pb_B2 >= 3:# dopracować?
            najmniejszy_czas.zmien_stacje_bazowa_na_B1()
            print(f"Osoba {najmniejszy_czas.id} zmieniła stację bazową na {najmniejszy_czas.stacja_bazowa}, moc z B1 {Pb_B1} a z B2 {Pb_B2}")

    elif czas_systemu == czas_ogolny:
        if len(kolejka.kolejka) < kolejka.max_rozmiar:
            czas = czas_ogolny + 20
            osoba = Osoba(czas)
            kolejka.dodaj_osobe(osoba)
            print("Nowa osoba dodana do kolejki. Czas :", czas)
            czas_ogolny += wyk.pop()  # 5
        elif len(kolejka2.kolejka2) < kolejka2.max_rozmiar:
            czas = czas_ogolny + 20
            osoba = Osoba(czas)
            kolejka2.dodaj_osobe(osoba)
            print("Nowa osoba dodana do kolejki2. Czas :", czas)
            czas_ogolny += wyk.pop()  # 5


    if czas_systemu >= 500:
        break
    if do_update:
        czas_systemu = 0
    else:
        do_update = True

print("-------------------")
print(Osoba.pobierz_licznik())
print("-------------------")
print(Osoba.pobierz_licznik_przelaczen())
print("-------------------")
kolejka.wypisz_kolejke()
print("-------------------")
print("k_2")
#kolejka2.wypisz_kolejke()

