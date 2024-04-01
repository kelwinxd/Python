
def Multiply(*args):
    total = 1
    


    for n in args:
        total *=n
    
    print(total, type(args))
    if total % 2 == 0:
        print('is even')

Multiply(2,5,7,6)