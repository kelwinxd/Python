
pessoa = {}


key = 'name'

pessoa[key] = 'kelwin'
pessoa['lastname'] = 'esechiel'

del pessoa['lastname']



print(pessoa[key])


#print(pessoa.get('lastname','Não existe '))
#pessoa.get() é como uma condicional, o segundo valor padrão é none
#Usar apenas if não para o error do programa, deve-se usar o .get
if pessoa.get('lastname') is None:
    print('Não Existe')
else:
    print(pessoa['lastname'])