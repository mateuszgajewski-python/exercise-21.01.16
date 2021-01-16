oceny =     {
                "Adam": {'oceny': (2,1,2,3,2,3), 'zachowanie': 4},
                "Kamil": {'oceny': (4,5,3,4,4,5), 'zachowanie': 3}
            }

for kluczDuzy in oceny:                                 #pobieram kluczDuzy
    print(kluczDuzy)                                    #wypisuje kluczDuzy
    for kluczMaly in oceny[kluczDuzy]:                  #pobieram nazwy kluczyMalych z kluczaDuzego
        print(kluczMaly, oceny[kluczDuzy][kluczMaly])   #wypisanie nazwy kluczaMalego i odczytanie wartosci tegoż klucza (do odczytania potrzebny jest kluczDuzy i kluczMaly)
    print()
