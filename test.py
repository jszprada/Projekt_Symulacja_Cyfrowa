from gaussa import random_gaussian
from row import random_uniform
from wyk import random_exponential
class Osoba:
    def __init__(self, czas):
        global ID
        self.id = ID
        self.czas = czas
        self.droga = 0

    def wypisz_dane(self):
        print(f"Id: {self.id}, czas: {self.czas}, droga: {self.droga}")

class Kolejka:
    def __init__(self):
        self.kolejka = []
        self.max_rozmiar = 5
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

czas_ogolny = 0
czas_systemu = 0
kolejka = Kolejka()
ID = 1
do_update = True

while True:
    if not kolejka.kolejka:
        czas = czas_ogolny + 1
        osoba = Osoba(czas)
        kolejka.dodaj_osobe(osoba)
        czas_ogolny += random_exponential(44)
        print(f"Osoba {osoba.id} dodana do kolejki. Czas:", czas)

    najmniejszy_czas = min(kolejka.kolejka, key=lambda x: x.czas)
    if czas_ogolny == najmniejszy_czas.czas:
        do_update = False

    czas_systemu = min(najmniejszy_czas.czas, czas_ogolny) #or czas_ogolny
    print("Czas ogolny:", czas_ogolny)
    print("Czas min obiektow:", najmniejszy_czas.czas)
    print("Czas systemu:", czas_systemu)

    if czas_systemu == najmniejszy_czas.czas:
        najmniejszy_czas.wypisz_dane()
        najmniejszy_czas.czas += 10
        najmniejszy_czas.droga += 0.02*random_uniform(44)
        if najmniejszy_czas.droga >= 40:
            kolejka.usun_osobe(najmniejszy_czas)
            print(f"Osoba {najmniejszy_czas.id, najmniejszy_czas.czas, najmniejszy_czas.droga} dotarła do celu")
        else:
            print("Czas po zmianie:", najmniejszy_czas.czas)

    elif czas_systemu == czas_ogolny and len(kolejka.kolejka) < kolejka.max_rozmiar:
        czas = czas_ogolny + 5
        osoba = Osoba(czas)
        kolejka.dodaj_osobe(osoba)
        print("Nowa osoba dodana do kolejki. Czas :", czas)

    if czas_systemu >= 30:
        break

    if do_update:
        czas_ogolny += random_exponential(44)
        czas_systemu = 0
    else:
        do_update = True

print("-------------------")
print(random_gaussian(44,1))
kolejka.wypisz_kolejke()
