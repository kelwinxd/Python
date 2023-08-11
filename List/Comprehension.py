
#metodo 1
print(list(range(10)))

#metodo 2
lista = []
for num in range(10):
    lista.append(num)
print(lista)

#metodo 3, list comprehension
#show the reverse list
lista2 = [abs(n - 10) for n in range(10)]

print(lista2)


