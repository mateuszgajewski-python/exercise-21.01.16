ludzie =    {
                "jghsafhsdvfhvsdfvkj": {'name': 'Mateusz', 'age': 30},
                "fgdffgfghdhfghddfhh": {'name': 'Aga', 'age': 32},
                "sfgdfgdfydgdhyhdbdt": {'name': 'Marcin', 'age': 12},
                "hfghjfdjfyfyjyfxhyt": {'name': 'Jola', 'age': 34},
                "hthfhyxfjytjdxjyxjg": {'name': 'Marek', 'age': 23}
            }

for duzyKlucz in ludzie:
    print(duzyKlucz)
    for malyKlucz in ludzie[duzyKlucz]:
        print(malyKlucz, ludzie[duzyKlucz][malyKlucz])
    print()
                
