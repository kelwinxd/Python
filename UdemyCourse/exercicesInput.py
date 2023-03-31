"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.


"""


numb = input("Type a int Number: ")

if numb.isdigit():
 numbInt = int(numb)
 EvenorOdd = numbInt % 2 == 0
 TextEorO = "Odd"
 if EvenorOdd:
  TextEorO = "Even"
 
  print(f'Your number {numbInt} is {TextEorO}')

else:
 print("You didnt type Int number")











"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

Hours = int(input("What time is it? "))

if Hours <= 11 :
 print("Morning")
elif Hours >= 12 and Hours <= 18:
 print("Evenning")
elif Hours >= 18 and Hours <=23:
 print("Night")
 




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Whats your name?")


try:

 if len(nome) >= 0 and len(nome) <= 4:
  print("Short Name")
 elif len(nome) >= 5 and len(nome) <= 6:
  print("Normal Name")
 elif len(nome) > 6:
  print("Huge Name")
 else:
  print('Unknown format')

except:
 print("Unknown Character!")


