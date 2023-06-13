from faker import Faker
import copy

fake = Faker()


dic1 = {
    'name':fake.name(),
    'age':18
}
#copy.copy() copia só items imutaveis como string etc, shallow copy, copia rasa
#deepcopy copia tudo até mutaveis
dic2 = copy.deepcopy(dic1)
dic2['age'] = 89


print(dic1)

print(dic2)