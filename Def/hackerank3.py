
n = int(input())

def operation(x):
  if not (isinstance(x, int) and 1 <= x <= 20):
    print('Forneça um número inteiro no intervalo de 1 a 20.')
  else:
    numbers = [i**2 for i in range(x)]
    for i in numbers:
        print(i)

operation(n)