from gaussa import RandomGaussianGenerator
from row import RandomUniformGenerator
from wyk import RandomExponentialGenerator
from oblicz_moc import oblicz_Pb_B1
from oblicz_moc import oblicz_Pb_B2
from przenoszenie_z_kolejki_do_kolejki import przenies_z_kolejki2_do_kolejki1

# --------------Odległości-------------------
x = 2000
B2_location = 5000
koniec_drogi = 3000
# ---------------Czas_raportu------------------
czas_raportowania = 20  # ms
# ---------------Handover------------------
ttt = 3  # ttt=1 to 20ms,
alfa = 3
wyrzucenie = -20
# ---------------Faza_lambda------------------
faza_pocz = 5
lambd = 1250
# ---------------zestawy_seedów------------------
s1 = [787663, 85432, 217999, 536714]
s2 = [246634, 562475, 914972, 547932]
s3 = [34436, 874091, 369383, 541165]
s4 = [180606, 521173, 939206, 884386]
s5 = [441758, 352312, 231343, 387603]
s6 = [634204, 306809, 184866, 442306]
s7 = [699631, 530573, 464552, 836097]
s8 = [870048, 33872, 772434, 282061]
s9 = [889042, 870289, 303972, 605645]
s10 = [126487, 941058, 852386, 749015]
seeds = s1
# ---------------Ograniczenie_symulacji------------------
l_osob_stop = 104  # +1 ->200
# ---------------generatory------------------
generator1 = RandomGaussianGenerator(seed=seeds[0])
generator2 = RandomGaussianGenerator(seed=seeds[1])
generator3 = RandomExponentialGenerator(seed=seeds[2], scale=lambd)
generator4 = RandomUniformGenerator(seed=seeds[3])
# ---------------stała_perdkość------------------
p_stala = 55
# ---------------zmiene_pomocnicze------------------
ID = 1
czas_ogolny = 0
czas_systemu = 0
srednia_odleglosc = 0
rozlaczenia = 0
wyznacz_poczatek = 0
przeleczenie = 0
droga_srednia = 0
# ---------------------------------

"""nazwa_pliku='sc1000_10'
def toFile(name, value):
    with open(name, "a") as file:
        file.write(str(value) + "\n")"""


class Osoba:
    licznik_osob = 0
    licznik_osob_usunietych = 0

    def __init__(self, czas, stacja_bazowa=1):
        global ID
        self.id = ID
        self.czas = czas
        self.droga = x
        self.ttt_up = 0
        self.stacja_bazowa = stacja_bazowa
        self.licznik_przelaczen = 0
        Osoba.licznik_osob += 1

    @staticmethod
    def pobierz_licznik():
        return Osoba.licznik_osob

    @staticmethod
    def pobierz_licznik_osob_usunietych():
        return Osoba.licznik_osob_usunietych

    def pobierz_licznik_przelaczen(self):
        return self.licznik_przelaczen

    def pobierz_ttt_up(self):
        return self.ttt_up

    def zwieksz_ttt_up(self, wartosc):
        self.ttt_up += wartosc

    def ustaw_ttt_up_zero(self):
        self.ttt_up = 0

    def zmien_stacje_bazowa_na_B2(self):
        if self.stacja_bazowa == 1:
            self.stacja_bazowa = 2
            self.licznik_przelaczen += 1
        else:
            pass

    def zmien_stacje_bazowa_na_B1(self):
        if self.stacja_bazowa == 2:
            self.stacja_bazowa = 1
            self.licznik_przelaczen += 1
        else:
            pass

    def wypisz_dane(self):
        print(f"Id: {self.id}, czas: {self.czas}, droga: {self.droga},stacja_bazowa: {self.stacja_bazowa}, ttt: {self.ttt_up}")


class Kolejka:
    def __init__(self):
        self.kolejka = []
        self.max_rozmiar = 20
        self.id = 0

    def dodaj_osobe(self, osoba):
        if len(self.kolejka) <= self.max_rozmiar:
            self.id += 1
            osoba.id = self.id
            self.kolejka.append(osoba)
        else:
            pass

    def usun_osobe(self, osoba):
        self.kolejka.remove(osoba)
        Osoba.licznik_osob_usunietych += 1

    def wypisz_kolejke(self):
        for osoba in self.kolejka:
            osoba.wypisz_dane()

    def liczba_uzytkownikow(self):
        return len(self.kolejka)


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

    def liczba_uzytkownikow2(self):
        return len(self.kolejka2)


# --------------- Kolejki ------------------
kolejka = Kolejka()
kolejka2 = Kolejka2()
# --------------- Flagi ------------------
do_update = True
sprawdz_warunkowe = True
# --------------- Dodanie_1_osoby ------------------
czas_z = czas_ogolny + czas_raportowania
osoba = Osoba(czas_z)
kolejka.dodaj_osobe(osoba)
print(f"Osoba {osoba.id} dodana do kolejki. Czas:", czas_z)
random_wyk = generator3()
czas_ogolny += random_wyk
# --------------- Pętla_głowna ------------------
while True:
    # --------------- wyznaczanie_czasu_symulacji ------------------
    najmniejszy_czas = min(kolejka.kolejka, key=lambda x: x.czas)
    if czas_ogolny == najmniejszy_czas.czas:
        do_update = False
    czas_systemu = min(najmniejszy_czas.czas, czas_ogolny)

    # --------------- Zdarzenia_czasowe-Raport_użytkownika ------------------
    if czas_systemu == najmniejszy_czas.czas:
        random_row = generator4()
        najmniejszy_czas.droga += 0.02 * random_row  # 50
        najmniejszy_czas.czas += czas_raportowania
        Pb_B1 = oblicz_Pb_B1(najmniejszy_czas.droga, generator1)
        Pb_B2 = oblicz_Pb_B2(B2_location - najmniejszy_czas.droga, generator2)
        sprawdz_warunkowe = False

    # --------------- Zdarzenia_warunkowe-Użytkownik_wyszedł_z_systemu ------------------
    if sprawdz_warunkowe == False and najmniejszy_czas.droga >= koniec_drogi:
        # print(f"W systemie {kolejka.liczba_uzytkownikow()}")
        # a=kolejka.liczba_uzytkownikow()
        # b=kolejka2.liczba_uzytkownikow2()
        # c=a+b
        # toFile(nazwa_pliku,c)
        if Osoba.pobierz_licznik_osob_usunietych() > faza_pocz:
            przeleczenie += najmniejszy_czas.licznik_przelaczen

        kolejka.usun_osobe(najmniejszy_czas)
        wyznacz_poczatek += 1
        # print(f"Liczba usunietych {wyznacz_poczatek}")
        sprawdz_warunkowe = True
        if len(kolejka2.kolejka2) > 0:
            przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny)
            # print(f"Osoba {najmniejszy_czas.id, najmniejszy_czas.czas, najmniejszy_czas.droga} dotarła do celu")
            # print(f"W systemie po dodaniu {kolejka.liczba_uzytkownikow()}")

    # --------------- Zdarzenia_warunkowe-Użytkownik_stracił_połączenie ------------------
    if sprawdz_warunkowe == False and Pb_B1 - Pb_B2 <= wyrzucenie and najmniejszy_czas.stacja_bazowa == 1:
        # print(f"W systemie {kolejka.liczba_uzytkownikow()}")
        # a = kolejka.liczba_uzytkownikow()
        # b = kolejka2.liczba_uzytkownikow2()
        # c = a + b
        # toFile(nazwa_pliku,c)
        if Osoba.pobierz_licznik_osob_usunietych() > faza_pocz:
            rozlaczenia += 1
            przeleczenie += najmniejszy_czas.licznik_przelaczen
        kolejka.usun_osobe(najmniejszy_czas)
        sprawdz_warunkowe = True
        # print(f"Osoba {najmniejszy_czas.id} straciła połączenie")
        if len(kolejka2.kolejka2) > 0:
            przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny)
            # print(f"W systemie po dodaniu {kolejka.liczba_uzytkownikow()}")

    if sprawdz_warunkowe == False and Pb_B2 - Pb_B1 <= wyrzucenie and najmniejszy_czas.stacja_bazowa == 2:
        # print(f"W systemie {kolejka.liczba_uzytkownikow()}")
        # a = kolejka.liczba_uzytkownikow()
        # b = kolejka2.liczba_uzytkownikow2()
        # c = a + b
        # toFile(nazwa_pliku,c)

        if Osoba.pobierz_licznik_osob_usunietych() > faza_pocz:
            rozlaczenia += 1
            przeleczenie += najmniejszy_czas.licznik_przelaczen
        kolejka.usun_osobe(najmniejszy_czas)
        sprawdz_warunkowe = True
        # print(f"Osoba {najmniejszy_czas.id} straciła połączenie")
        if len(kolejka2.kolejka2) > 0:
            przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny)
            # print(f"W systemie po dodaniu {kolejka.liczba_uzytkownikow()}")

    # ttt_up = najmniejszy_czas.pobierz_ttt_up()
    # print(ttt_up)

    # --------------- Zdarzenia_warunkowe-Użytkownik_przełącza_się_do_stacji_bazowej ------------------
    if sprawdz_warunkowe == False and Pb_B2 > Pb_B1 and abs(Pb_B2 - Pb_B1) >= alfa:
        sprawdz_warunkowe = True
        if najmniejszy_czas.stacja_bazowa == 1:
            ttt_up = najmniejszy_czas.pobierz_ttt_up()
            if ttt_up == ttt:
                najmniejszy_czas.ustaw_ttt_up_zero()
                # print("Zeruje po handover_to_B2 == True and ttt_up == ttt:")
                najmniejszy_czas.zmien_stacje_bazowa_na_B2()
                # print(f"Osoba {najmniejszy_czas.id} zmieniła stację bazową na {najmniejszy_czas.stacja_bazowa}, moc z B1 {Pb_B1} a z B2 {Pb_B2}")
                if Osoba.pobierz_licznik_osob_usunietych() > 5:
                    droga_srednia += najmniejszy_czas.droga
            else:
                najmniejszy_czas.zwieksz_ttt_up(1)
        elif najmniejszy_czas.stacja_bazowa == 2:
            najmniejszy_czas.ustaw_ttt_up_zero()
            # print("Zeruje po najmniejszy_czas.stacja_bazowa==2")
    # ttt_up = najmniejszy_czas.pobierz_ttt_up()
    # print(ttt_up)
    if sprawdz_warunkowe == False and Pb_B1 > Pb_B2 and abs(Pb_B1 - Pb_B2) >= alfa:
        sprawdz_warunkowe = True
        if najmniejszy_czas.stacja_bazowa == 2:
            ttt_up = najmniejszy_czas.pobierz_ttt_up()
            if ttt_up == ttt:
                najmniejszy_czas.ustaw_ttt_up_zero()
                # print("Zeruje po handover_to_B1 == True and ttt_up == ttt")
                najmniejszy_czas.zmien_stacje_bazowa_na_B1()
                # print(f"Osoba {najmniejszy_czas.id} zmieniła stację bazową na {najmniejszy_czas.stacja_bazowa}, moc z B1 {Pb_B1} a z B2 {Pb_B2}")
                if Osoba.pobierz_licznik_osob_usunietych() > 5:
                    droga_srednia += najmniejszy_czas.droga
            else:
                najmniejszy_czas.zwieksz_ttt_up(1)
        elif najmniejszy_czas.stacja_bazowa == 1:
            najmniejszy_czas.ustaw_ttt_up_zero()
            # print("Zeruje po najmniejszy_czas.stacja_bazowa==1")
    # ttt_up = najmniejszy_czas.pobierz_ttt_up()
    # print(ttt_up)
    if sprawdz_warunkowe == False and abs(Pb_B1 - Pb_B2) < alfa:
        sprawdz_warunkowe = True
        najmniejszy_czas.ustaw_ttt_up_zero()
        # print("Zeruje po abs(Pb_B1 - Pb_B2) < 3")
    # ttt_up = najmniejszy_czas.pobierz_ttt_up()
    # print(ttt_up)

    # --------------- Zdarzenia_czasowe-Dodanie_użytkownika_do_systemu ------------------
    if czas_systemu == czas_ogolny:
        if len(kolejka.kolejka) < kolejka.max_rozmiar:
            czas = czas_ogolny + czas_raportowania
            osoba = Osoba(czas)
            kolejka.dodaj_osobe(osoba)
            random_wyk = generator3()
            czas_ogolny += random_wyk  # 5
        elif len(kolejka2.kolejka2) < kolejka2.max_rozmiar:
            czas = czas_ogolny + czas_raportowania
            osoba = Osoba(czas)
            kolejka2.dodaj_osobe(osoba)
            random_wyk = generator3()
            czas_ogolny += random_wyk  # 5

    # --------------- warunki_zakonczenia_petli ------------------
    if Osoba.licznik_osob_usunietych > l_osob_stop:
        break

    if do_update:
        czas_systemu = 0
    else:
        do_update = True

L_przelaczen = przeleczenie
sr_od_przelaczenia = droga_srednia / L_przelaczen
print("-------------------srednia odległośc")
print(sr_od_przelaczenia)
print("-------------------rozlaczenia")
print(rozlaczenia)
l_usunietych = Osoba.pobierz_licznik_osob_usunietych() - faza_pocz
print(f"liczba uzykowników po odjeci poczatkowgo {l_usunietych}")
srednia_roz = rozlaczenia / l_usunietych
print("------------------- srednia_rozlaczen")
print(srednia_roz)
print("------------------- stworzeni uzytkownicy")
print(Osoba.pobierz_licznik())
print("------------------- przełączenia")
print(przeleczenie)
print("------------------- srednia przełączenia na uzytkownika")
print(przeleczenie / l_usunietych)
print("------------------- usunieci z systemu")
print(Osoba.pobierz_licznik_osob_usunietych())
print("-------------------")
#kolejka.wypisz_kolejke()
print("-------------------")
print("kolejka_2")
#kolejka2.wypisz_kolejke()
