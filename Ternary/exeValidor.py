import re
import sys
import geratorCPF
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
gerared = geratorCPF.justNine
cpf = '122.151.992-19'






#para gerar o Primeiro digito do CPF

cpfPolite = (cpf.replace('.','').replace('-','').replace('',' ').strip(' ').split(' ')) 
#ou use expressão regular 
cpfPolitetoo = re.sub(
    r'[^0-9]',
    '',
    cpf
)

isSeq = cpf == cpf[0] * len(cpf)
if isSeq:
    print('voce digitou numeros sequenciais')
    sys.exit()


justNine = cpfPolite[:9]
counter = 11
total1 = 0



for n in justNine:
    counter -= 1
    total1 += counter * int(n)



digito1 = (total1 * 10) % 11

verify = digito1 if digito1 <= 9 else 0




#para gerar o Segundo digito do CPF

cpfPolite = (cpf.replace('.','').replace('-','').replace('',' ').strip(' ').split(' '))

justTen = cpfPolite[:10]
counter = 12
total1 = 0


for n in justTen:
    counter -= 1
    total1 += counter * int(n)



digito2 = (total1 * 10) % 11

verify = digito2 if digito2 <= 9 else 0




cpf2 = ''.join(justNine)
new_cpf = f'{cpf2}{digito1}{digito2}'


final_verify = 'Válido' if new_cpf == ''.join(cpfPolite) else 'Não Válido'

print(final_verify)









    
    

     
    
    
    






