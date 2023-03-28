

Valor1 = input('Type a Value: ')
Valor2 = input('Type a Value Again: ')

def major(Valor1, Valor2):
    if int(Valor1)>int(Valor2):
        print(f'{Valor1}')
    elif int(Valor2)>int(Valor1):
        print(f'{Valor2}')

major(Valor1,Valor2)
