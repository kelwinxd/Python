andif = 10 == 11

condicao = 'Valor' if andif else 'Outro Valor'


teste = input("Digite um ano: ")
resposta = teste if len(teste) <= 4 else "Digite um ano válido"

print(resposta)