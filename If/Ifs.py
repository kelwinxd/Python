import random

#Conditions

a=random.randrange(0,100)
b=random.randrange(0,100)

result=0
op="-"
Phrase=""

if op=="+":
    result=a+b
elif op=="-":
    result=a-b

if result % 2 == 0:
    Phrase="Even Number"
else: 
    Phrase="Odd Number"
 
     



Equation= "{} {} {} = {} \n {}"
print(Equation.format(a,op,b,result, Phrase))

