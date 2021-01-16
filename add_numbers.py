suma = 0
x = 0

while x < 3:
    liczba = int(input("Podaj liczbe dodatnia i jednocześnie parzysta "))
    if(liczba > 0 and liczba%2 == 0):
        suma += liczba
    else:
        print("err")
        continue
    x += 1
    
print("suma", suma)


    
