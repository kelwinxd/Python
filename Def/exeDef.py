#create a function which multiply all numbers set

def Multi(*args):
    total = 1
    args = list(args)
    for n in args:
        total *= int(n)
    return total
    


print(Multi(2,30,10))


def evenorOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


print(evenorOdd(9))


 #recursive call   
def fator(n):
    if n == 0:
        return 1
    else:
        return n * fator(n-1)
    
print(fator(5))