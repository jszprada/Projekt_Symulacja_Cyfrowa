def przenies_z_kolejki2_do_kolejki1(kolejka2, kolejka, czas_ogolny):
    pierwsza_osoba = kolejka2.kolejka2.pop(0)
    pierwsza_osoba.czas = czas_ogolny + 20
    kolejka.dodaj_osobe(pierwsza_osoba)
    # print("Osoba przeniesiona z kolejki 2 do kolejki 1")
