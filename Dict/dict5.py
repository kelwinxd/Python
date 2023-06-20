# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

dic1 = {
    'name':'Kelwin',
    'age':25
}

#update a dict
dic1.update(height=1.85,weight=78)
docs = [['birth','28-04-1998'],['age',26]]
dic1.update(docs)

print(dic1)

#del a key
dic1.pop('height')

print(dic1.get('height',''))
for key,value in dic1.items():
    print(f'{key}: {value}')

