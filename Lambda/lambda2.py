def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
# no recommended if it gets difficult to read
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ), # thats the same of def soma(2,3)
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)




print(
    executa(
        lambda p, name: f'{p}, {name}!', 'good morning', 'Kelwin'
    )
    #one line code
)