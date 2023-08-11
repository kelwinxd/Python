def generator(n = 0, maxx=0):
    n = int(input('Input number 1: '))
    maxx = int(input('Input number 2:'))
    
    while True:
        yield n
        n +=2
        if n > maxx:
            return

    

gen = generator()
num = 0
array = []
for n in gen:
    print(n)
    array.append(n)
    

qt = len(array)

print(f'tem {qt} de numeros ímpares entre {array[0]} e {array[-1]}')
