oceny =     [
                {'imie': 'Adam', 'oceny': (2,1,2,3,2,3), 'zachowanie': 5},
                {'imie': 'Kamil', 'oceny': (3,4,5,3,4,5), 'zachowanie': 2}
            ]


for slownik in oceny:               #wczytanie  slownika z listy 
    for klucz in slownik:           #pobranie nazwy klucza 
        print(klucz,' -> ', slownik[klucz])  #wypisanie nazwy klucza i wartości tegoż klucza
    print()
