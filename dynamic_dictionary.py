bazaSlow = {}

while(1):
    x=0
    slowo = ""
    definicja = ""
    print()
    print("1 - podaj nowe słowo i definicje")
    print("2 - podaj slowo i poznaj definicje")
    print("3 - usuń słowo z definicja")
    print("4 - podgląd bazy")
    print()
    x = input("Podaj wybór : ")
    print()
    
    if x == '1':
        print("Wybraleś - 1")
        slowo = input("Podaj slowo ")
        print("Podaj definicja slowa, ", slowo)
        definicja = input()
        bazaSlow[slowo] = definicja
        print(slowo, " - ", definicja, " ZAPISANO :)")

        
    elif x == '2':
        print("Wybraleś - 2")
        slowo = input("Podaj slowo ")
        
        if bazaSlow.get(slowo):
            print(bazaSlow[slowo])
            
        else:
            print("nie ma definicji dla tego slowa")

            
    elif x == '3':
        print("Wybraleś - 3")
        slowo = input("Podaj slowo ")
        
        if(bazaSlow.get(slowo)):
           bazaSlow.pop(slowo)
           print(slowo, '<- USUNIĘTO')
           
        else:
            print("TAKIEGO CZEGOŚ NIE MOGE USUNĄĆ BO NIE ISTNIEJE!!!")

           
    elif x == '4':
        for klucz in bazaSlow:
            print(klucz, " - ", bazaSlow[klucz])

            
    elif x == "exit":
        break

    
    else:
        print("Podaj co chcesz zrobić!!!")
        continue
    
    
        
        
        
    
