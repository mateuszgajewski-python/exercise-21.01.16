sekret = 88

while(1):
    x = int(input("\n zgadnij liczbe :"))
    if(sekret < x):
        print("\n Liczba za duza, sprobuj ponownie")
        continue
    elif(sekret > x):
        print("\n Liczba za mala, sprobuj ponownie")
        continue
    else:
        print("\n zgadles, sekret to ", sekret)
        break

