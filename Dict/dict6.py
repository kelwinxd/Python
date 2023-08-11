people = {
    'nome':'jordan',
    'lastname':'michael',
}

#desempacotando o dict
(a1,a2), (b1,b2) = people.items()

print(a1,a2 + '\n' + b1,b2)

for key, value in people.items():
    print(f'{key}: {value}')

#args e desempack
#kwargs use two **

complete_people = {**people, 'age': 24}
print(complete_people)


#creating a function to show the obj with kwargs
def show_integer(*args,**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

show_integer(**complete_people)

