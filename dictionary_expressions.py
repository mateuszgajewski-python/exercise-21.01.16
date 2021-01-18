names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': 20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

nameLenght =    {
    name : len(name)
    for name in names
    if name.startswith("A")
                }
multipliedNumbers =     {
    number : number*number
    for number in numbers
                        }
potegaTrzecia =   {
    number : number ** 3
    for number in numbers
                }
zCelciusNaF =   {
    key : celcius * 1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20
                }
