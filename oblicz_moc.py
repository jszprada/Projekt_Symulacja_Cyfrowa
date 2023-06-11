import math


def oblicz_Pb_B1(d, generator):
    s = generator()
    return 4.56 - 22 * math.log10(d) + s


def oblicz_Pb_B2(d, generator):
    s = generator()
    return 4.56 - 22 * math.log10(d) + s
