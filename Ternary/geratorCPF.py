import re
import sys
import random


justNine = ''

for num in range(9):
     justNine += str(random.randint(0,9))



counter = 11
total = 0

for i in justNine:
   counter -=1
   total += counter * int(i)

result = (total * 10) % 11
digit1 = result if result <= 9 else 0


counter2 = 12
total2 = 0
cpfAlmost = f'{justNine}{digit1}'
for a in cpfAlmost:
    counter2 -=1
    total2 = counter2 * int(a)

result2 = (total2 * 10) % 11
digit2 = result2 if result2 <= 9 else 0

Cpf = f'{justNine}-{digit1}{digit2}'
print(digit2)
print(Cpf)







    
    

     
    
    
    






