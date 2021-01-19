names = {"arkadiusz", "Wioletta", "karol", "bartlomiej", "Jakub", "Anna"}


names2 =    {
    name.capitalize()
    for name in names        
            }

names3 =    {
    name.capitalize()
    for name in names
    if not (name.startswith("B") or name.startswith("b"))
            }

'''
names =         {
    names.discard(name)
    for name in names
    if (name.startswith("B") or name.startswith("b"))
               }
'''

#nie mozna uzyc discard z forem na secie
