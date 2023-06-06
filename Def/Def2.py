#Named Parameter


#When you declare a function argument by providing a default value, if the
# parameter is empty, it will take on this default value.

def Sum(a,b,c=None):
    if c is not None:
     print(f'{a=} {b=} {c=} | a+b+c = ', a+b+c)
    else:
       print(f'{a=} {b=} | a+b= ', a+b)
     


Sum(2,5)

def Velo(d,t):
   return d / t



print(Velo(500, 10))