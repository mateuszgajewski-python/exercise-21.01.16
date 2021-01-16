liczby = [1, 2, 3, 4]


potegiDwojki =      [element**2     for element in liczby]

liczbyParzyste =    [element        for element in liczby   if (element % 2 == 0)]
#                        ^                   |                        ^         |
#                        |                   |                        |         |
#                        |                   |___dla elemntów sprawdza warunek  |
#                        |                                                      |
#                        |__________________I ROBI TO___________________________|                                            


print(potegiDwojki)
print()
print(liczbyParzyste)
