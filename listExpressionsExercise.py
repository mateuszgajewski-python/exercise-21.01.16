#znajdz liczby od 100 do 470 wlacznie
#ktore sa podzielne przez 7 a nie są podzielne przez 5


listaLiczb =    [
        liczba
        for liczba in range(100, 471)
        if liczba % 7 == 0
        if not liczba % 5 == 0
                ]
