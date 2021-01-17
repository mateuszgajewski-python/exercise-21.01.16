evenNumbersGenerator = (    element     for element in range(100)   if(element % 2 == 0)    )


print(sum(evenNumbersGenerator))


evenNumbersGenerator2 = (    element**2     for element in range(101)    )


print(sum(evenNumbersGenerator2))





